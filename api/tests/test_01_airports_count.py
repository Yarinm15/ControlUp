import requests
from api.utils import config, constants

def test_airport_count():
    response = requests.get(f"{config.BASE_URL}/airports")
    assert response.status_code == 200, "Expected status code 200"

    data = response.json().get("data", [])
    assert len(data) == constants.EXPECTED_AIRPORT_COUNT, \
        f"Expected {constants.EXPECTED_AIRPORT_COUNT} airports, got {len(data)}"
    
