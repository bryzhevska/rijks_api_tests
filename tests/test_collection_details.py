import allure

from api.endpoints import RijksmuseumAPI
from api.schemas.object_detail_schema import ObjectDetailResponse
from api.validator import validate_with_model


@allure.feature("Collection Details")
@allure.story("Retrieve collection object by valid object number")
def test_get_object_by_valid_number():
    client = RijksmuseumAPI()
    detail_response = client.get_object_details_by_object_number(f"SK-C-597")
    assert detail_response.status_code == 200
    validate_with_model(ObjectDetailResponse, detail_response.json())


@allure.feature("Collection Details")
@allure.story("Retrieve collection object by invalid object number")
def test_get_object_by_invalid_number():
    client = RijksmuseumAPI()
    response = client.get_object_details_by_object_number(f"INVALID-ID")
    assert response.status_code == 400
