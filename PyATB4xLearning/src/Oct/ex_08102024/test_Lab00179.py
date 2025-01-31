#API Request - HTTP Request
# Create Booking

import pytest
import allure
import requests


@allure.title("TC#1 - Create Booking CRUD Positive")
@allure.description("TC#1 - Verify the create booking!")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    # To make Request
    # URL
    # Method - POST
    # Headers - Content-type=Application/json - Dict
    # Payload / Data / Body - Dict / JSON
    # Auth(No)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type" : "application/json"}
    payload = {
        "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : False,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01",
        },
        "additionalneeds" : "Breakfast",
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200   #-Status code

    responseData = response.json()

    # Response Body Verification
    # Headers
    # Status Code

    bookingid = responseData["bookingid"]
    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int


    firstname = responseData["booking"]["firstname"]
    lastname = responseData["booking"]["lastname"]
    totalprice = responseData["booking"]["totalprice"]
    depositpaid = responseData["booking"]["depositpaid"]

    assert firstname == "Jim"
    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == False

    checkin = responseData["booking"]["bookingdates"]["checkin"]
    checkout = responseData["booking"]["bookingdates"]["checkout"]

    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"


# JSON Scheme Validation
# Time response



@allure.title("TC#2 - Create Booking CRUD Negative")
@allure.description("TC#2 - Verify Booking is not created with {} data")
@pytest.mark.crud
def test_create_booking_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type" : "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    #Assertions
    assert response.status_code == 500




@allure.title("TC#3 - Negative Create Booking CRUD Negative")
@allure.description("TC#3 - Verify Booking with totalprice string negatgive")
@pytest.mark.crud
def test_create_booking_negative_tc3():              #if we pass -1 or "Wasim" getting 200 OK -> It's a Bug to report.
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type" : "application/json"}
    json_payload = {
        "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : "Wasim",
        "depositpaid" : False,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01",
        },
        "additionalneeds" : "Breakfast",
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)

    #Assertions
    assert response.status_code == 200



