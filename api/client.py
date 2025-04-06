import os

import requests
from dotenv import load_dotenv

from .logger import logger

load_dotenv()


class RijksmuseumClient:
    BASE_URL = "https://www.rijksmuseum.nl/api/en"

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("RIJKSMUSEUM_API_KEY")
        if not self.api_key:
            raise ValueError("API key is missing. Set RIJKSMUSEUM_API_KEY in .env or pass it directly.")

    def get(self, path: str, params: dict = None):
        if params is None:
            params = {}
        params["key"] = self.api_key
        params["format"] = "json"

        url = f"{self.BASE_URL}/{path}"
        logger.info(f"Sending GET request to {url} with params: {params}")
        response = requests.get(url, params=params)

        logger.debug(f"Response [{response.status_code}]: {response.text[:300]}")

        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            logger.error(f"[HTTP ERROR] {e} - {response.text}")
            raise
        return response
