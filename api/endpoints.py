from .client import RijksmuseumClient
from .schemas.collection_schema import CollectionResponse
from .schemas.object_detail_schema import ObjectDetailResponse


class RijksmuseumAPI:
    def __init__(self, api_key: str = None):
        self.client = RijksmuseumClient(api_key)

    def get_collection(self, params=None) -> CollectionResponse:
        if params is None:
            params = {}
        response = self.client.get("collection", params=params)
        return response

    def get_object_details_by_object_number(self, object_number: str) -> ObjectDetailResponse:
        response = self.client.get(f"collection/{object_number}")
        return response
