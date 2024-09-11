import pytest

from selenium import webdriver

from page_object.login_page import LoginPage, AddToCartPage, PayItemPage, FinishPage
from urls import Urls


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def add_to_cart_page(driver):
    return AddToCartPage(driver)


@pytest.fixture
def pay_item_page(driver):
    return PayItemPage(driver)


@pytest.fixture
def finish_page(driver):
    return FinishPage(driver)
