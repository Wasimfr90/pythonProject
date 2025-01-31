# PUT request :
# URL
# Path - Booking ID
# Token - Auth
# Payload
# Headers


import pytest
import allure
import requests


#Create a Token - POST
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type" : "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)

    responseData = response.json()
    token = responseData["token"]

    #token = response.json()["token"]  # also same as above 2 lines
    print(token)
    return token


#Create Booking - POST
def create_booking():
    print("Create Booking Testcase")
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01",
        },
        "additionalneeds": "Breakfast",
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    print(type(url))
    print(type(headers))
    print(type(json_payload))

    #Assertion
    assert response.status_code == 200
    # get the response Body and Verify the JSON, Booking ID is not None
    data = response.json()
    bookingid = data["bookingid"]
    return bookingid




# PUT request test case
def test_put_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())

    PUT_URL = base_url + base_path
    cookie = "token=" + create_token()
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



def test_delete():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    DELETE_URL = URL + str(booking_id)
    cookie_value = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "cookie": cookie_value,
    }
    print(headers)

    response = requests.delete(url=DELETE_URL, headers=headers)
