import pytest
from selenium import webdriver


# Фикстура для драйвера Chrome
@pytest.fixture()
def driver_Firefox():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


# Фикстура для драйвера Chrome
@pytest.fixture()
def driver_Chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
