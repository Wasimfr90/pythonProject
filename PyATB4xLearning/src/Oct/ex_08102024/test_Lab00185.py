import pytest
import requests
import allure


def test_update_request_1(create_token, create_booking):
    print("Token ->", create_token)
    print("Booking ID - >", create_booking)

    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking)

    PUT_URL = base_url + base_path
    cookie = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "cookie": cookie,
    }

    json_payload = {
        "firstname": "Wasim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01",
        },
        "additionalneeds": "Breakfast",
    }

    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Wasim"
