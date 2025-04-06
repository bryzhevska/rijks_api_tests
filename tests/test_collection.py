import allure

from api.endpoints import RijksmuseumAPI
from api.schemas.collection_schema import CollectionResponse
from api.validator import validate_with_model


@allure.feature("Collection")
@allure.story("Retrieve collection list by requested size")
def test_get_collection_by_specified_size():
    api = RijksmuseumAPI()
    response = api.get_collection({"ps": 15})
    assert response.status_code == 200
    validate_with_model(CollectionResponse, response.json())
    response_data = CollectionResponse.model_validate_json(response.text)
    assert len(response_data.artObjects) == 15


@allure.feature("Collection")
@allure.story("Search for collection object by first maker")
def test_search_by_first_maker():
    client = RijksmuseumAPI()
    collection_response = client.get_collection({"q": "Rembrandt+van+Rijn"})
    assert collection_response.status_code == 200

    validate_with_model(CollectionResponse, collection_response.json())
    response_data = CollectionResponse.model_validate_json(collection_response.text)

    for art_object in response_data.artObjects:
        assert art_object.title is not None, f"Title is missing in artObject {art_object.id}"
        assert "Rembrandt van Rijn" in art_object.principalOrFirstMaker, \
            f"Expected 'Rembrandt van Rijn' as principalOrFirstMaker, but got {art_object.principalOrFirstMaker}"


@allure.feature("Collection")
@allure.story("Retrieve collection list by default size")
def test_get_collection_by_default_size():
    api = RijksmuseumAPI()
    response = api.get_collection()
    assert response.status_code == 200

    validate_with_model(CollectionResponse, response.json())
    response_data = CollectionResponse.model_validate_json(response.text)
    assert len(response_data.artObjects) == 10
