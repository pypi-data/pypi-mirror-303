from typing import List,Optional

import httpx
import requests
import io

from loguru import logger

from tgshops_integrations.nocodb_connector.model_mapping import ID_FIELD


def custom_key_builder(func, *args, **kwargs):
    # Exclude 'self' by starting args processing from args[1:]
    args_key_part = "-".join(str(arg) for arg in args[1:])
    kwargs_key_part = "-".join(f"{key}-{value}" for key, value in sorted(kwargs.items()))
    return f"{func.__name__}-{args_key_part}-{kwargs_key_part}"


class NocodbClient:
      
    def __init__(self,NOCODB_HOST=None,NOCODB_API_KEY=None,SOURCE=None):
        self.NOCODB_HOST = NOCODB_HOST
        self.NOCODB_API_KEY = NOCODB_API_KEY
        self.SOURCE=SOURCE
        self.httpx_client = httpx.AsyncClient(timeout=60.0)
        self.httpx_client.headers = {
            "xc-token": self.NOCODB_API_KEY
        }

    def construct_get_params(self,
                             required_fields: list = None,
                             projection: list = None,
                             extra_where: str = None,
                             offset: int = None,
                             limit: int = None) -> dict:
        extra_params = {}
        if projection:
            extra_params["fields"] = ','.join(projection)
        if required_fields:
            extra_params["where"] = ""
            for field in required_fields:
                extra_params["where"] += f"({field},isnot,null)~and"
            extra_params["where"] = extra_params["where"].rstrip("~and")
        if extra_where:
            if not extra_params.get("where"):
                extra_params["where"] = extra_where
            else:
                extra_params["where"] += f"~and{extra_where}"
        if offset:
            extra_params['offset'] = offset
        if limit:
            extra_params["limit"] = limit
        return extra_params

    async def get_table_records(self,
                                table_name: str,
                                required_fields: list = None,
                                projection: list = None,
                                extra_where: str = None,
                                limit: int = None) -> List[dict]:
        url = f"{self.NOCODB_HOST}/tables/{table_name}/records"
        extra_params = self.construct_get_params(required_fields, projection, extra_where, limit=limit)
        response = await self.httpx_client.get(url, params=extra_params)
        if response.status_code == 200:
            return response.json()["list"]
        raise Exception(response.text)

    async def get_table_records_v2(self,
                                   table_name: str,
                                   required_fields: list = None,
                                   projection: list = None,
                                   extra_where: str = None,
                                   offset: int = None,
                                   limit: int = 25) -> dict:
        url = f"{self.NOCODB_HOST}/tables/{table_name}/records"
        extra_params = self.construct_get_params(required_fields, projection, extra_where, offset=offset, limit=limit)
        response = await self.httpx_client.get(url, params=extra_params)
        if response.status_code == 200:
            return response.json()
        raise Exception(response.text)

    async def get_table_record(self,
                               table_name: str,
                               record_id: str,
                               required_fields: list = None,
                               projection: list = None) -> dict:
        url = f"{self.NOCODB_HOST}/tables/{table_name}/records/{record_id}"
        extra_params = self.construct_get_params(required_fields, projection)
        response = await self.httpx_client.get(url, params=extra_params)
        if response.status_code == 200:
            return response.json()
        raise Exception(response.text)

    async def create_table_record(self, table_name: str, record: dict) -> dict:
        url = f"{self.NOCODB_HOST}/tables/{table_name}/records"
        response = await self.httpx_client.post(url, json=record)
        if response.status_code == 200:
            record["id"] = response.json().get("id")
            if not record["id"]:
                record["id"] = response.json().get("Id")
            return record
        raise Exception(response.text)

    async def count_table_records(self, table_name: str) -> int:
        url = f"{self.NOCODB_HOST}/tables/{table_name}/records/count"
        response = await self.httpx_client.get(url)
        if response.status_code == 200:
            return response.json().get("count", 0)
        raise Exception(response.text)

    async def update_table_record(self, table_name: str, record_id: str, updated_data: dict) -> bool:        
        url = f"{self.NOCODB_HOST}/tables/{table_name}/records"
        updated_data[ID_FIELD] = int(record_id)
        if updated_data["ID"]:
            updated_data.pop("ID")
        response = await self.httpx_client.patch(url, json=updated_data)
        if response.status_code == 200:
            return True
        raise Exception(response.text)

    async def delete_table_record(self, table_name: str, record_id: str) -> dict:
        url = f"{self.NOCODB_HOST}/tables/{table_name}/records"
        response = requests.delete(url, json={"Id": record_id}, headers=self.httpx_client.headers)
        if response.status_code == 200:
            logger.info(f"Deleted item {record_id}")
        return response.json()

    # Not transport
    async def get_product_categories(self, table_id: str,table_name : str) -> int:
        url = f"{self.NOCODB_HOST}/tables/{table_id}/records"
        limit=75
        extra_params = self.construct_get_params(limit=limit)
        response = await self.httpx_client.get(url, params=extra_params)

        if response.status_code == 200:
            categories={category[table_name] : category["Id"] for category in response.json()["list"]}
            return categories
        raise Exception(response.text)
        return {}
        
    
    
    async def create_product_category(self, table_id: str, category_name : str, table_name : str, category_id : int = 0)  -> dict:
        url = f"{self.NOCODB_HOST}/tables/{table_id}/records"

        record={table_name: category_name, "Id" : category_id}

        response = await self.httpx_client.post(url, json=record)
        if response.status_code == 200:
            self.categories = await self.get_product_categories(table_id=table_id, table_name=table_name)
            return record
        raise Exception(response.text)
    
    async def get_table_meta(self, table_name: str):
        return (await self.httpx_client.get(
            f"{self.NOCODB_HOST.replace('/api/v2', '/api/v1')}/db/meta/tables/{table_name}")).json()


    async def get_all_tables(self, source: Optional[str] = None):
        if not source:
            source=self.SOURCE

        url = f"{self.NOCODB_HOST.replace('/api/v2', '/api/v1')}/db/meta/projects/{source}/tables?includeM2M=false"
        response=(await self.httpx_client.get(url)).json()
        tables_info=response.get('list', [])
        self.tables_list={table["title"] : table["id"] for table in tables_info}
        return self.tables_list

    async def get_sources(self):
        return (await self.httpx_client.get(
            f"{self.NOCODB_HOST.replace('/api/v2', '/api/v1')}/db/meta/projects/")).json().get(
            'list', [])
    
    async def get_table_meta(self, table_name: str):
        return (await self.httpx_client.get(
            f"{self.NOCODB_HOST.replace('/api/v2', '/api/v1')}/db/meta/tables/{table_name}")).json()
    

    async def create_table_column(self, table_name: str, name: str):
        return (await self.httpx_client.post(
            f"{self.NOCODB_HOST.replace('/api/v2', '/api/v1')}/db/meta/tables/{table_name}/columns",
            json={
                "column_name": name,
                "dt": "character varying",
                "dtx": "specificType",
                "ct": "varchar(45)",
                "clen": 45,
                "dtxp": "45",
                "dtxs": "",
                "altered": 1,
                "uidt": "SingleLineText",
                "uip": "",
                "uicn": "",
                "title": name
            })).json()

    async def link_table_record(
            self,
            base_id: str,
            fk_model_id: str,
            record_id: str,
            source_column_id: str,
            linked_record_id: str) -> dict:
        """
        base_id
        fk_model_id - ID of linked column
        record_id - ID of source record to be linked
        source_column_id -ID of source column
        linked_record_id - ID of linked record

        POST /api/v1/db/data/noco/pwb8m0yee7nvw6m/mtk2pg9eiix11qs/242/mm/ct5sskewp6sg54q/91
        /fk_model- smr8uvm11kurzprp
        """
        url = f"{self.NOCODB_HOST.replace('/api/v2', '/api/v1')}/db/data/noco/{base_id}/{fk_model_id}/{record_id}/mm/{source_column_id}/{linked_record_id}"
        response = await self.httpx_client.post(url,headers=self.httpx_client.headers)
        if response.status_code == 200:
            return response.json()
        raise Exception(response.text)

    async def unlink_table_record(
            self,
            base_id: str,
            fk_model_id: str,
            record_id: str,
            source_column_id: str,
            linked_record_id: str) -> dict:
        """
        base_id
        fk_model_id - ID of linked column
        record_id - ID of source record to be linked
        source_column_id -ID of source column
        linked_record_id - ID of linked record

        POST /api/v1/db/data/noco/pwb8m0yee7nvw6m/mtk2pg9eiix11qs/242/mm/ct5sskewp6sg54q/91
        """
        path = f"{self.NOCODB_HOST.replace('/api/v2', '/api/v1')}/db/data/noco/{base_id}/{fk_model_id}/{record_id}/mm/{source_column_id}/{linked_record_id}"
        response = await self.httpx_client.delete(path)
        if response.status_code == 200:
            return response.json()
        raise Exception(response.text)

    async def save_image_to_nocodb(
            self,
            image_url: str,
            image_name: str,
            source_column_id: str,
            product_table_name: str,
            images_column_id: str) -> dict:
        """
        source
        fk_model_id - ID of linked column
        record_id - ID of source record to be linked
        source_column_id -ID of source column
        linked_record_id - ID of linked record
        """

        response = requests.get(image_url)
        if response.status_code == 200:
            file = io.BytesIO(response.content)
        else:
            raise Exception(f"Failed to fetch the image. Status code: {response.status_code}")
        
        file_size = file.getbuffer().nbytes

        if file_size:

            files = {'file': (image_name, file, 'image/jpeg')}

            url = f"{self.NOCODB_HOST.replace('/api/v2', '/api/v1')}/db/storage/upload?path=noco/{source_column_id}/{product_table_name}/{images_column_id}"
            timeout = httpx.Timeout(100.0)
            response = await self.httpx_client.post(url,files=files,headers=self.httpx_client.headers,timeout=timeout)
            if response.status_code == 200:
                return response.json()[0]['url']
            raise Exception(response.text)
        else:
            return ""