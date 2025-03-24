# consume fixture from conftest.py

import pytest

@pytest.fixture()
def create_token():
    return "abc"


@pytest.fixture()
def create_booking_id():
    return 123


def test_update_request_1(create_token, create_booking_id):
    print("Token ->", create_token)
    print("Booking ID - >", create_booking_id)

def test_update_request_2(create_token, create_booking_id):
    print("Token ->", create_token)
    print("Booking ID - >", create_booking_id)