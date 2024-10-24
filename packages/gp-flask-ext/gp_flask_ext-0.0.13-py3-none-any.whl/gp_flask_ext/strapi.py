import requests
from loguru import logger

class StrapiClient:
    def __init__(self, url: str, identifier: str, password: str, **kwargs):
        self.base_url = url
        self.identifier = identifier
        self.password = password
        self.session = requests.Session()
        self.api_key = None
        self.config = kwargs
        if self.identifier and self.password:
            self.login()

    def _get_headers(self):
        if self.api_key:
            headers = {
                "Authorization": f"Bearer {self.api_key}"
            }
        else:
            headers = {}
        return headers

    def login(self):
        url = f"{self.base_url}/auth/local"
        data = {
            "identifier": self.identifier,
            "password": self.password
        }
        response = self.session.post(url, json=data)
        if response.status_code == 200:
            self.api_key = response.json()["jwt"]
        else:
            self.api_key = None

    def get(self, endpoint: str, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        if kwargs:
            url += "?" + "&".join([f"{k}={v}" for k, v in kwargs.items()])
        logger.info("GET: {}", url)
        headers = self._get_headers()
        response = self.session.get(url, headers=headers)
        return response.json()
    
    def add(self, endpoint: str, data: dict):
        url = f"{self.base_url}/{endpoint}"
        headers = self._get_headers()
        response = self.session.post(url, json=data, headers=headers)
        return response.json()