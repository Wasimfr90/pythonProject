
import pytest
import requests

@pytest.fixture()
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


@pytest.fixture()
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


@pytest.fixture()
def read_csv_file_data():
    pass

@pytest.fixture()
def read_myself_file_database():
    pass

@pytest.fixture()
def launch_browser():
    print("Launching a Browser!!! Chrome")
    return "Chrome"

@pytest.fixture()
def close_browser():
    print("Closing a Browser!!! Chrome")
    return "Closed"

@pytest.fixture()
def read_url_testdata_excel():
    pass