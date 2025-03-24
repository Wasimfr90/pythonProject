# Restful booker Update request -PUT
# For Update we need to create Token -> create booking -> update booking -> delete booking
from http.client import responses

import pytest
import allure
import requests



@allure.title("TC for Update request")
@allure.testcase("#TC-2")


def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type" : "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response_data = requests.post(url=url, headers=headers, json=payload)
    response_val = response_data.json()

    token = response_val["token"]
    print(token)
    return token

def create_booking():
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
    print(type(complete_url))
    print(type(actual_headers))
    print(type(payload))

    create_resp = response_data.json()
    booking_id = create_resp["bookingid"]
    return booking_id


#PUT request testcase
@pytest.mark.crud
def test_put_req_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    actual_url = base_url + base_path
    cookie = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie,
    }

    put_payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 99999,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-03-10",
            "checkout": "2025-03-15"
        },
        "additionalneeds": "Breakfast"
    }
    put_response = requests.put(url=actual_url, headers=headers, json=put_payload)
    assert put_response.status_code == 200
    print(put_response.status_code)

    output_response = put_response.json()
    print(output_response)
    first_name = output_response["firstname"]
    total_price = output_response["totalprice"]

    assert first_name == "James"
    assert total_price == 99999


@pytest.mark.crud
def test_delete():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    total_url = base_url + base_path

    cookie = "token=" + create_token()
    del_header = {
        "Cookie": cookie,
    }
    del_response = requests.delete(url=total_url, headers=del_header)
    print("delete status code: ", del_response.status_code)

# Note - here in delete function tc, it's creating one token then one new create booking then deleteing it. Not the updated one.







