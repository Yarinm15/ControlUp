import requests
from api.utils import config, constants

def test_distance_between_kix_and_nrt():
    url = f"{config.BASE_URL}/airports/distance"

    payload = constants.DISTANCE_PAYLOAD_KIX_TO_NRT

    response = requests.post(url, json=payload)
    assert response.status_code == 200, "Expected status code 200"

    distance_km = response.json()["data"]["attributes"]["kilometers"]
    assert distance_km > constants.DISTANCE_MIN_KM, \
        f"Expected distance > {constants.DISTANCE_MIN_KM} km, got {distance_km}"

