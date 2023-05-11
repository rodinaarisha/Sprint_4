import pytest
from selenium import webdriver

@pytest.fixture()
def driver():

    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver

    driver.quit()
