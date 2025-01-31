#GET booking testcase
#Verify that booking is not null
#status code, header ...

#Request module - request


import pytest
import allure
import requests

@allure.title("Test GET Request - RestFUL BOOKER project#1")
@allure.description("TC#1 -> Verify the GET request with ID works")
@allure.tag("regression","p0","smoke")
@allure.label("owner","Wasim Firoj Rahaman")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id_positive():
    url = "https://restful-booker.herokuapp.com/booking/1"
    respose_data = requests.get(url)
    print(respose_data.text)
    print(respose_data.json())
    print(respose_data.headers)
    assert respose_data.status_code == 200


@allure.title("Test GET Request - RestFUL BOOKER project#2")
@allure.description("TC#2 -> Verify the GET request with invalid ID works")
@pytest.mark.smoke
def test_get_single_request_by_id_negative1():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    respose_data = requests.get(url)
    assert respose_data.status_code == 404


@allure.title("Test GET Request - RestFUL BOOKER project#3")
@allure.description("TC#3 -> Verify the GET request with invalid ID works")
@pytest.mark.smoke
def test_get_single_request_by_id_negative2():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    respose_data = requests.get(url)
    assert respose_data.status_code == 404


@allure.title("Test GET Request - RestFUL BOOKER project#4")
@allure.description("TC#4 -> Verify the GET request with special character ID works")
@pytest.mark.smoke
def test_get_single_request_by_id_negative3():
    url = "https://restful-booker.herokuapp.com/booking/@#$%"
    respose_data = requests.get(url)
    assert respose_data.status_code == 404
