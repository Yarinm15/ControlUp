import requests
from api.utils import config, constants

def test_specific_airports_present():
    response = requests.get(f"{config.BASE_URL}/airports")
    assert response.status_code == 200, "Expected status code 200"

    data = response.json().get("data", [])
    airport_names = []

    for airport in data:
        name = airport["attributes"]["name"]
        airport_names.append(name)
        
    for expected_airport in constants.EXPECTED_AIRPORTS:
        assert expected_airport in airport_names, \
            f"{expected_airport} not found in response"
