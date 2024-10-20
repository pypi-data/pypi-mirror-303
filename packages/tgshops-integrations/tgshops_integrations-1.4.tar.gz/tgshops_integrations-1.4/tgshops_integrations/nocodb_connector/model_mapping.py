import json
import secrets

import markdown

from tgshops_integrations.models.categories import CategoryModel
from tgshops_integrations.models.products import ExtraAttribute, ProductModel
from tgshops_integrations.models.categories import CategoryResponseModel,PaginationResponseModel
from tgshops_integrations.models.products import  ProductModel

import importlib.util
from pathlib import Path


# Helper function to load config.py dynamically
def load_config(config_path):
    config_path = Path(config_path)
    if config_path.exists():
        spec = importlib.util.spec_from_file_location("config", config_path)
        config = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config)
        return config
    else:
        raise FileNotFoundError(f"Configuration file not found at {config_path}")

# Modify this to accept config_path dynamically
def initialize_model_mapping(config_path):
    global CATEGORY_IMAGE_FIELD, ID_FIELD, CATEGORY_NAME_FIELD, CATEGORY_PARENT_ID_FIELD, CATEGORY_PARENT_FIELD,CATEGORY_ID_OF_CATEGORY_FIELD
    global PRODUCT_NAME_FIELD, PRODUCT_DESCRIPTION_FIELD, PRODUCT_PRICE_FIELD, PRODUCT_CURRENCY_FIELD, PRODUCT_STOCK_FIELD
    global PRODUCT_CATEGORY_NAME_FIELD, PRODUCT_CATEGORY_ID_FIELD, PRODUCT_IMAGE_FIELD, PRODUCT_DISCOUNT_PRICE_FIELD
    global PRODUCT_CATEGORY_ID_LOOKUP_FIELD, PRODUCT_REQUIRED_OPTIONS_FIELD, PRODUCT_CATEGORIES_EXTRA_OPTIONS_FIELD
    global PRODUCT_CATEGORIES_EXTRA_OPTION_NAMES_FIELD, PRODUCT_EXTRA_CHOICE_REQUIRED_FIELD, PRODUCT_ID_FIELD
    global PRODUCT_EXTERNAL_ID, PRODUCT_CHECKOUT_MODE, NEW_ID_FIELD, NOCODB_CHECKOUT_MODES
    
    config = load_config(config_path)
    
    # Step 3: Load all required constants from config.py
    CATEGORY_IMAGE_FIELD = config.CATEGORY_IMAGE_FIELD
    ID_FIELD = config.ID_FIELD
    CATEGORY_NAME_FIELD = config.CATEGORY_NAME_FIELD
    CATEGORY_PARENT_ID_FIELD = config.CATEGORY_PARENT_ID_FIELD
    CATEGORY_PARENT_FIELD = config.CATEGORY_PARENT_FIELD
    CATEGORY_ID_OF_CATEGORY_FIELD = config.CATEGORY_ID_OF_CATEGORY_FIELD

    PRODUCT_NAME_FIELD = config.PRODUCT_NAME_FIELD
    PRODUCT_DESCRIPTION_FIELD = config.PRODUCT_DESCRIPTION_FIELD
    PRODUCT_PRICE_FIELD = config.PRODUCT_PRICE_FIELD
    PRODUCT_CURRENCY_FIELD = config.PRODUCT_CURRENCY_FIELD
    PRODUCT_STOCK_FIELD = config.PRODUCT_STOCK_FIELD
    PRODUCT_CATEGORY_NAME_FIELD = config.PRODUCT_CATEGORY_NAME_FIELD
    
    PRODUCT_CATEGORY_ID_FIELD = config.PRODUCT_CATEGORY_ID_FIELD
    PRODUCT_IMAGE_FIELD = config.PRODUCT_IMAGE_FIELD
    PRODUCT_DISCOUNT_PRICE_FIELD = config.PRODUCT_DISCOUNT_PRICE_FIELD
    PRODUCT_CATEGORY_ID_LOOKUP_FIELD = config.PRODUCT_CATEGORY_ID_LOOKUP_FIELD
    PRODUCT_REQUIRED_OPTIONS_FIELD = config.PRODUCT_REQUIRED_OPTIONS_FIELD
    PRODUCT_CATEGORIES_EXTRA_OPTIONS_FIELD = config.PRODUCT_CATEGORIES_EXTRA_OPTIONS_FIELD
    PRODUCT_CATEGORIES_EXTRA_OPTION_NAMES_FIELD = config.PRODUCT_CATEGORIES_EXTRA_OPTION_NAMES_FIELD
    PRODUCT_EXTRA_CHOICE_REQUIRED_FIELD = config.PRODUCT_EXTRA_CHOICE_REQUIRED_FIELD
    PRODUCT_ID_FIELD = config.PRODUCT_ID_FIELD
    PRODUCT_EXTERNAL_ID = config.PRODUCT_EXTERNAL_ID
    PRODUCT_CHECKOUT_MODE = config.PRODUCT_CHECKOUT_MODE
    NEW_ID_FIELD = config.NEW_ID_FIELD

    NOCODB_CHECKOUT_MODES = config.NOCODB_CHECKOUT_MODES


def get_pagination_info(page_info: dict) -> PaginationResponseModel:
    page_info = PaginationResponseModel(total_rows=page_info['totalRows'],
                                        page=page_info['page'],
                                        page_size=page_info['pageSize'],
                                        is_first_page=page_info['isFirstPage'],
                                        is_last_page=page_info['isLastPage'])
    return page_info

def parse_category_data(data: dict) -> CategoryResponseModel:
    preview_url = ""
    if data.get(CATEGORY_IMAGE_FIELD):
        preview_url = data[CATEGORY_IMAGE_FIELD][0].get("url", "")
    return CategoryResponseModel(
        id=str(data[ID_FIELD]),
        name=data.get(CATEGORY_NAME_FIELD, ""),
        parent_category=str(data.get(CATEGORY_PARENT_ID_FIELD, 0)),
        preview_url=preview_url,
    )


def dump_category_data(data: CategoryModel) -> dict:
    return {
        CATEGORY_NAME_FIELD: data.name,
        CATEGORY_PARENT_FIELD: data.parent_category,
        CATEGORY_IMAGE_FIELD: [
            {"url": data.preview_url, 'title': f'{secrets.token_hex(6)}.jpeg', 'mimetype': 'image/jpeg'}]
    }


def dump_product_data(data: ProductModel) -> dict:

    preview_url = ([{'url': image_url,
                     'title': f'{secrets.token_hex(6)}.jpeg',
                     'mimetype': 'image/jpeg'}
                    for image_url in data.preview_url]
                   if data.preview_url
                   else [])

    return {
        PRODUCT_NAME_FIELD: data.name,
        PRODUCT_DESCRIPTION_FIELD: data.description,
        PRODUCT_PRICE_FIELD: data.price,
        PRODUCT_CURRENCY_FIELD: data.currency,
        PRODUCT_STOCK_FIELD: data.stock_qty,
        PRODUCT_CATEGORY_NAME_FIELD:[data.category_name] if data.category_name else None,
        PRODUCT_CATEGORY_ID_FIELD: [{'Id': data.category}] if data.category else None,
        PRODUCT_IMAGE_FIELD: preview_url,
        PRODUCT_DISCOUNT_PRICE_FIELD: data.final_price
    }

def dump_product_data_with_check(data: ProductModel, data_check: dict) -> dict:
 
    preview_url = ([{'url': image_url,
                    'title': f'{secrets.token_hex(6)}.jpeg',
                    'mimetype': 'image/jpeg'}
                for image_url in data.preview_url]
                if data.preview_url
                else [])
    
    extra_data = {item.name : item.description for item in data.extra_attributes}

    product_data = {
        PRODUCT_ID_FIELD: data.id,
        PRODUCT_EXTERNAL_ID: data.external_id,
        PRODUCT_NAME_FIELD: data.name,
        PRODUCT_DESCRIPTION_FIELD: data.description,
        PRODUCT_PRICE_FIELD: data.price,
        PRODUCT_CURRENCY_FIELD: data.currency,
        PRODUCT_STOCK_FIELD: data.stock_qty,
        PRODUCT_CATEGORY_NAME_FIELD:[data.category_name] if data.category_name else None,
        PRODUCT_CATEGORY_ID_FIELD: [{'Id': data_check[item]} for item in data.category_name] if data.category else None,
        PRODUCT_IMAGE_FIELD: preview_url,
        PRODUCT_CHECKOUT_MODE: NOCODB_CHECKOUT_MODES,
        PRODUCT_DISCOUNT_PRICE_FIELD: data.final_price,
        }
    
    if len(extra_data)>0:
        product_data.update(extra_data)
    return product_data


async def parse_product_data(data: dict) -> ProductModel:
    preview_url = [image['url'] for image in data[PRODUCT_IMAGE_FIELD]] if data.get(PRODUCT_IMAGE_FIELD, '') else []
    primary_keys = [ID_FIELD,PRODUCT_NAME_FIELD, PRODUCT_DESCRIPTION_FIELD, PRODUCT_PRICE_FIELD,
                    PRODUCT_CURRENCY_FIELD, PRODUCT_STOCK_FIELD, PRODUCT_CATEGORY_ID_FIELD, PRODUCT_IMAGE_FIELD,
                    PRODUCT_CATEGORY_NAME_FIELD, PRODUCT_DISCOUNT_PRICE_FIELD, PRODUCT_CATEGORY_ID_LOOKUP_FIELD,
                    PRODUCT_REQUIRED_OPTIONS_FIELD, PRODUCT_CATEGORIES_EXTRA_OPTIONS_FIELD,
                    PRODUCT_CATEGORIES_EXTRA_OPTION_NAMES_FIELD, PRODUCT_EXTRA_CHOICE_REQUIRED_FIELD,
                    "UpdatedAt", "CreatedAt"]

    # Dynamically adding extra attributes
    extra_attributes = []
    for key, value in data.items():
        if key not in primary_keys and value is not None and type(value) in [str, int, float]:
            extra_attributes.append(ExtraAttribute(name=key, description=str(value)))

    product = ProductModel(
        id=str(data[ID_FIELD]) if data.get(ID_FIELD) else data.get(NEW_ID_FIELD),
        external_id=data.get(PRODUCT_EXTERNAL_ID, ""),
        name=data.get(PRODUCT_NAME_FIELD, ""),
        description=data.get(PRODUCT_DESCRIPTION_FIELD, "") if data.get(PRODUCT_DESCRIPTION_FIELD) else "",
        price=data.get(PRODUCT_PRICE_FIELD, 0.0),
        currency=data.get(PRODUCT_CURRENCY_FIELD, ["RUB","CZK","GBP"]) if data.get(PRODUCT_CURRENCY_FIELD) else "RUB",
        stock_qty=data.get(PRODUCT_STOCK_FIELD, 0),
        preview_url=preview_url,
        category_name=data.get(PRODUCT_CATEGORY_NAME_FIELD, []) if data.get(PRODUCT_CATEGORY_NAME_FIELD) else [],
        category=data.get(PRODUCT_CATEGORY_ID_LOOKUP_FIELD, []) if data.get(PRODUCT_CATEGORY_ID_LOOKUP_FIELD) else [],
        # category=[],
        extra_attributes=extra_attributes,
        extra_option_choice_required=any(data.get(PRODUCT_EXTRA_CHOICE_REQUIRED_FIELD, [])),
        metadata = data
    )
    if data.get(PRODUCT_DISCOUNT_PRICE_FIELD, data.get(PRODUCT_PRICE_FIELD, 0.0)):
        product.final_price = data.get(PRODUCT_DISCOUNT_PRICE_FIELD, data.get(PRODUCT_PRICE_FIELD, 0.0))
    
    return product




