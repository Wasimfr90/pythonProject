# Fixture - Concept of Python

# You can give context to the test, by using Fixture.
# Similar - pre-condition, post condition (What do we need to put in before test and after test)

# Pre Condition - token, booking id - Fixture -> it will be common to all test cases under the .py file
# Ex - For PUT request we need to create token and booking id, which we can keep it in Fixture.
# test_Update_negative 1
# test_Update_positive 2


import pytest

@pytest.fixture()
def is_married():
    return True


def test_i_need_confirm(is_married):
    assert is_married== False

