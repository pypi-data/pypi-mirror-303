import os
import requests
from loguru import logger

def get_nocodb_client_from_env(env_file=".nocodb.env") -> 'NocodbClient':
    """Get nocodb client from environment variables.

    Environment variables:
        - NOCODB_URL: nocodb url
        - NOCODB_API_TOKEN: nocodb api token
        - NOCODB_PROJECT_ID: nocodb project id
    """
    try:
        import dotenv
        ret = dotenv.load_dotenv(env_file)
        logger.debug("dotenv found: {} {}", env_file, ret)
    except:
        logger.warning("dotenv not found.")


    NOCODB_URL = os.environ['NOCODB_URL']
    NOCODB_API_TOKEN = os.environ['NOCODB_API_TOKEN']
    NOCODB_PROJECT_ID = os.environ['NOCODB_PROJECT_ID']

    db = NocodbClient(NOCODB_URL, NOCODB_API_TOKEN, NOCODB_PROJECT_ID)
    return db

class NocodbClient:
    """NocodbClient is a client for nocodb api.
    
    查询返回的数据格式如下：
    {   
        'list': [{'Id': 1}], 
        'pageInfo': {
            'totalRows': 1, 
            'page': 1, 
            'pageSize': 25, 
            'isFirstPage': True, 
            'isLastPage': True}, 
        'stats': {'dbQueryTime': '11.463'}
    }
    """

    def __init__(self, url: str, api_token: str, project_id: str, **kwargs):
        self.base_url = url + "/api/v2"
        self.api_token = api_token
        self.project_id = project_id
        self.config = kwargs
        self.session = requests.Session()
        self.session.headers.update(self._get_headers())

    def _get_headers(self):
        if self.api_token:
            headers = {
                "xc-token": self.api_token
            }
        else:
            headers = {}
        return headers
    
    def get_projects(self):
        url = f"{self.base_url}/meta/bases/"
        headers = self._get_headers()
        response = self.session.get(url, headers=headers)
        return response.json()
    
    def get_tables(self, full_info=False):
        """Get tables in the project"""
        url = f"{self.base_url}/meta/bases/{self.project_id}/tables"
        headers = self._get_headers()
        response = self.session.get(url, headers=headers)
        resp = response.json()
        tables = {}
        if "error" in resp:
            logger.error(resp)
            return tables
        for item in resp["list"]:
            tables[item["title"]] = item if full_info else item["id"]
        return tables
    
    def get_table_metadata(self, table_id):
        """Get table metadata"""
        url = f"{self.base_url}/meta/tables/{table_id}"
        response = self.session.get(url)
        return response.json()
    
    def get_table_links(self, table_id, full_info=False):
        """Get table link fields"""
        coulmns = self.get_table_metadata(table_id).get("columns", [])
        links = {}
        for col in coulmns:
            if col["uidt"] in ("LinkToAnotherRecord", "Links"):
                links[col["title"]] = col if full_info else col["id"]
        return links
    
    def get_views(self, table_id):
        """Get tables in the project"""
        url = f"{self.base_url}/meta/tables/{table_id}/views"
        headers = self._get_headers()
        views = {}
        response = self.session.get(url, headers=headers)
        resp = response.json()
        if "error" in resp:
            logger.error(resp)
            return views
        for item in resp["list"]:
            views[item["title"]] = item["id"]
        return views
            

    def get(self, table_id, params: dict = None, view_id=None, fields=None, sort=None, offset=0, limit=25):
        """Get records from table
        ref: https://data-apis-v2.nocodb.com/#tag/Table-Records/operation/db-data-table-row-list
        
        Args:
            table_id: 表格id
            params: 查询参数, dict, 支持 where, sort, offset, limit, filds
                where: str, like "(field1,eq,value1)~and(field2,eq,value2)"
                sort: str, like "field1,-field2"
                filds: str or list, like "field1,field2"
                offset: int, default 0
                limit: int, default 25
            view_id: 视图id
            fields: 要查询的字段, str or list
            sort: 排序字段, str
            offset: 查询偏移量, 默认0
            limit: 查询条数, 默认25
        
        Returns:
            dict: response from nocode api
            list: [{"Id": 1}, {"Id": 2}]
            pageInfo: dict
                totalRows: int
                page: int
                pageSize: int
                isFirstPage: bool
                isLastPage: bool
        """
        url = f"{self.base_url}/tables/{table_id}/records"
        _params = {
            "offset": offset,
            "limit": limit,
            "where":"",
        }
        if view_id: _params["viewId"] = view_id
        if fields:
            if isinstance(fields, list): fields = ",".join(fields)  # list to str
            _params["fields"] = fields
        if sort: _params["sort"] = sort
        if params:
            _params.update(params)
        headers = self._get_headers()
        response = self.session.get(url, headers=headers, params=_params)
        resp = response.json()
        if "error" in resp:
            logger.error(resp)
        return resp
    
    def get_one(self, table_id, id):
        """Get one record from table"""
        url = f"{self.base_url}/tables/{table_id}/records/{id}"
        headers = self._get_headers()
        response = self.session.get(url, headers=headers)
        return response.json()
    
    def link(self, table_id, linkFieldId, recordId, ids):
        """Link record to table"""
        url = f"{self.base_url}/tables/{table_id}/links/{linkFieldId}/records/{recordId}"
        response = self.session.post(url, json=ids)
        resp = response.json()
        if type(resp) == "dict" and "error" in resp:
            logger.error(resp)
        return resp

    def add(self, table_id, rows):
        """Add records to table"""
        url = f"{self.base_url}/tables/{table_id}/records"
        headers = self._get_headers()
        response = self.session.post(url, headers=headers, json=rows)
        return response.json()
    
    def update(self, table_id, rows):
        """Update records in table"""
        url = f"{self.base_url}/tables/{table_id}/records"
        headers = self._get_headers()
        response = self.session.patch(url, headers=headers, json=rows)
        return response.json()
    
    def delete(self, table_id, ids):
        """Delete records from table"""
        url = f"{self.base_url}/tables/{table_id}/records"
        headers = self._get_headers()
        response = self.session.delete(url, headers=headers, json=ids)
        return response.json()
    
    def add_one(self, table_id, item, key="Id", attachments=None, update_if_exists=False):
        """Add one record to table, if the record exists, skip
        
        Args:
            table_id: table id
            item: record to add
            key: key to check if the record exists
            attachments: list of fields to upload as attachments

        Returns:
            dict: response from nocode api
        """
        url = f"{self.base_url}/tables/{table_id}/records"
        headers = self._get_headers()
        if key:
            # 只有指定了key才做排重检查
            _params = {
                "fields": "Id",
                "where": f"({key},eq,{item[key]})"
            }
            logger.debug("querying {}...", _params)
            r = self.session.get(url, headers=headers, params=_params).json()
            if r["pageInfo"]["totalRows"] > 0:
                #logger.debug("{} exists, skip", item[key])
                if update_if_exists:
                    item["Id"] = r["list"][0]["Id"]     # 使用第一个元素的Id, 用于更新
                    logger.debug("fatch item.id {}...", item)
                else:
                    logger.info("{} exists, skip", item[key])
                    return r
        if attachments:
            for attachment in attachments:
                file_to_upload = item[attachment]
                item[attachment] = self.upload_file(file_to_upload)
        if "Id" in item:
            logger.debug("updating {}...", item)
            response = self.session.patch(url, headers=headers, json=item)
        else:
            logger.debug("adding {}...", item)
            response = self.session.post(url, headers=headers, json=item)
        ret = response.json()
        if "msg" in ret:
            logger.error("error: {}", ret["msg"])
        return ret
    
    def upload_file(self, file_path):
        """Upload file to nocodb storage"""
        url = f"{self.base_url}/storage/upload"
        headers = self._get_headers()
        if isinstance(file_path, str):
            fd = open(file_path, "rb")
        else:
            fd = file_path
        files = {
            "file": fd      # TODO: file_name, mimetype
        }
        response = self.session.post(url, headers=headers, files=files)
        return response.json()
    
    def upload_file_tuple(self, file_tuple):
        """Upload file to nocodb storage
        
        Args:
            file_tuple: (file_path, file_name, mimetype)
            
        Returns: 
            dict: response from nocode api
        """
        url = f"{self.base_url}/storage/upload"
        headers = self._get_headers()
        files = {
            "file": file_tuple
        }
        response = self.session.post(url, headers=headers, files=files)
        return response.json()