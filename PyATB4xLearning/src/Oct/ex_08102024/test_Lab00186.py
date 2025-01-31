import pytest
import requests
import allure

def test_selenium(launch_browser, close_browser):
    launch_browser
    print("Do TC")
    close_browser
