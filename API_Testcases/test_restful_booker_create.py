# Restful Booker - CREATE request

import pytest
import allure
import requests

@allure.title("Restful Booker - Create Booking TC")
@allure.testcase("TC1")
@pytest.mark.crud
def test_create_booking_by_id_positive():
    # URL
    # Header
    # Method
    # Body or Payload

    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    complete_url = base_url + base_path
    actual_headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Wasim",
        "lastname": "Rahaman",
        "totalprice": 65995,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-03-01",
            "checkout": "2025-03-10"
        },
        "additionalneeds": "Breakfast"
    }
    response_data = requests.post(url=complete_url, headers=actual_headers, json=payload)
    assert response_data.status_code == 200

    response_body = response_data.json()
    booking_id = response_body["bookingid"]
    print(f"Booking id is : {booking_id}")
    assert booking_id is not None
    assert booking_id > 0
    assert type(booking_id) == int

    first_name = response_body["booking"]["firstname"]
    last_name = response_body["booking"]["lastname"]
    total_price = response_body["booking"]["totalprice"]

    assert first_name == "Wasim"
    assert last_name == "Rahaman"
    assert total_price == 65995

    checkin = response_body["booking"]["bookingdates"]["checkin"]
    checkout = response_body["booking"]["bookingdates"]["checkout"]

    assert checkin == "2025-03-01"
    assert checkout == "2025-03-10"
