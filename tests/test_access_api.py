import allure
import pytest

from api.client import RijksmuseumClient


@allure.feature("Authorization")
@allure.story("Request collection with invalid API key")
def test_invalid_key():
    client = RijksmuseumClient("INVALID")
    with pytest.raises(Exception):
        client.get("collection")
