from typing import List,Optional
import importlib.util
from pathlib import Path

from aiocache import cached
from tgshops_integrations.models.products import ProductModel
from tgshops_integrations.nocodb_connector.client import NocodbClient

from tgshops_integrations.nocodb_connector.model_mapping import dump_product_data,dump_product_data_with_check, get_pagination_info, ID_FIELD, \
    parse_product_data, PRODUCT_CATEGORY_ID_LOOKUP_FIELD, PRODUCT_NAME_FIELD, PRODUCT_PRICE_FIELD, \
    PRODUCT_STOCK_FIELD

from tgshops_integrations.nocodb_connector.categories import CategoryManager
from tgshops_integrations.nocodb_connector.products import ProductManager
from tgshops_integrations.nocodb_connector.tables import *
# from .config import NOCODB_CATEGORIES,NOCODB_PRODUCTS,NOCODB_STATUSES,NOCODB_BOT_MESSAGES,NOCODB_ORDERS

from loguru import logger

class Gateway(NocodbClient):

    def __init__(self,logging=False,NOCODB_HOST=None,NOCODB_API_KEY=None,SOURCE=None,filter_buttons=[],config_path=None,special_attributes=False):
        super().__init__(NOCODB_HOST=NOCODB_HOST,NOCODB_API_KEY=NOCODB_API_KEY,SOURCE=SOURCE)
        if config_path:
            self.load_config_from_path(config_path)

        self.logging = logging
        self.required_fields = [self.config.PRODUCT_NAME_FIELD, self.config.PRODUCT_PRICE_FIELD]
        self.projection = []
        self.special_attributes = special_attributes
        self.filter_buttons = filter_buttons

    def load_config_from_path(self,config_path):
        if config_path.exists():
            spec = importlib.util.spec_from_file_location("config", config_path)
            self.config = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(self.config)
        else:
            raise FileNotFoundError(f"Configuration file not found at {config_path}")

    async def load_data(self,SOURCE=None):
        self.SOURCE=SOURCE
        await self.get_all_tables()
        self.category_manager=CategoryManager(table_id=self.tables_list[self.config.NOCODB_CATEGORIES],NOCODB_HOST=self.NOCODB_HOST,NOCODB_API_KEY=self.NOCODB_API_KEY,logging=True,filter_buttons=self.filter_buttons)
        self.product_manager=ProductManager(table_id=self.tables_list[self.config.NOCODB_PRODUCTS],NOCODB_HOST=self.NOCODB_HOST,NOCODB_API_KEY=self.NOCODB_API_KEY,logging=True)

    async def create_product(self,product: ProductModel) -> ProductModel:
        products_table = self.tables_list[self.config.NOCODB_PRODUCTS]
        data = dump_product_data_with_check(data=product ,data_check=self.category_manager.categories)
        # product_json = dump_product_data_with_check(data=product,data_check=self.categories)
        external_id = data.pop("ID")
        metadata = await self.get_table_meta(self.tables_list["Products"])
        images_column=[column["id"] for column in metadata["columns"] if column["column_name"] == "Images"][0]
        data["ExternalImages"]=[image['title'] for image in data['Images']]

        for num,item in enumerate(data['Images']):
            url_before=item['url']
            image_name=item['title']
            data['Images'][num]['url']=await self.save_image_to_nocodb(source_column_id=self.SOURCE,image_url=url_before,image_name=image_name,product_table_name=products_table,images_column_id=images_column)

        record = await self.create_table_record(table_name=products_table, record=data)
        # logger.info(f"Created product {record['id']}")
        logger.info(f"Created product {external_id}")

    async def get_all_products(self):
        actual_products=[]
        products_portion=[]
        portion=200
        # TODO Check once busy
        for i in range(10):
            products_portion=await self.product_manager.get_products_v2(offset=i*portion,limit=portion)
            actual_products.extend(products_portion)
            if len(products_portion) < 200:
                break
        return actual_products
    
    async def update_products(self, external_products: List[ProductModel]):
        products_table = self.tables_list[self.config.NOCODB_PRODUCTS]
        await self.product_manager.update_attributes(products=external_products)
        # Updates categories if there were a new ones created
        external_products=await self.category_manager.map_categories(external_products=external_products)
        self.product_manager.actual_products=await self.get_all_products()
        # self.product_manager.actual_products = await self.product_manager.get_products_v2(offset=0,limit=200)

        self.ids_mapping={product.external_id : product.id for product in self.product_manager.actual_products}
        products_meta= {product.external_id : product for product in self.product_manager.actual_products}

        for product in external_products:
            if product.external_id in self.ids_mapping.keys():
                product.id=self.ids_mapping[product.external_id]
                if self.product_manager.hash_product(product,special_attributes=self.special_attributes)!=self.product_manager.hash_product(products_meta[product.external_id],special_attributes=self.special_attributes):
                    await self.update_product(product=product)
            else:
                await self.create_product(product=product)
        
    async def update_product(self, product: ProductModel):
        products_table = self.tables_list[self.config.NOCODB_PRODUCTS]
        data = dump_product_data_with_check(data=product ,data_check=self.category_manager.categories)

        await self.update_table_record(
            table_name=products_table,
            record_id=product.id,
            updated_data=data)
        logger.info(f"Updated product {product.external_id}")
        
        
    def find_product_id_by_name(self,name: str):
        for product in self.product_manager.actual_products.products:
            if product.name == name:
                return product.id
        return None  # Return None if no product is found with the given name
    
    async def delete_all_products(self):  
        items = await self.product_manager.get_products_v2(offset=0,limit=200)
        products_table = self.tables_list[self.config.NOCODB_PRODUCTS]    
        for num,item in enumerate(items):
            await self.delete_table_record(products_table, item.id)