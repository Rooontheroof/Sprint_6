import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def driver():
    driver = webdriver.Firefox()

    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    driver.quit()