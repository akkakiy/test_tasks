import allure

from data import Texts
from urls import Urls


@allure.suite('Проверки на авторизацию, добавление в корзину и оплату')
class TestPayItem:
    @allure.title('Авторизация пользователя')
    def test_login(self, driver, login_page):
        login_page.find_and_click_username_field()
        login_page.fill_in_username()
        login_page.find_and_click_password_field()
        login_page.fill_in_password()
        login_page.click_login_button()
        assert (login_page.get_url() == Urls.CATALOG_URL
                and
                login_page.find_text() == Texts.TEXT_CATALOG_PRODUCTS)

    @allure.title('Добавление товара в корзину')
    def test_add_to_cart(self, driver, login_page, add_to_cart_page):
        login_page.full_login()
        add_to_cart_page.find_and_click_product()
        add_to_cart_page.find_and_click_add_to_cart_button()
        add_to_cart_page.find_and_click_basket_button()
        assert (add_to_cart_page.find_item_name() == Texts.TEXT_ITEM_NAME
                and
                add_to_cart_page.find_item_price() == Texts.TEXT_ITEM_PRICE)

    @allure.title('Оплата')
    def test_pay_item(self, driver, login_page, add_to_cart_page, pay_item_page):
        login_page.full_login()
        add_to_cart_page.full_add_item_to_cart()
        pay_item_page.find_and_click_checkout_button()
        pay_item_page.find_and_click_first_name_field()
        pay_item_page.fill_first_name()
        pay_item_page.find_and_click_last_name_field()
        pay_item_page.fill_last_name()
        pay_item_page.find_and_click_zip_postal_code_field()
        pay_item_page.fill_zip_postal_code()
        pay_item_page.find_and_click_continue_button()
        assert (pay_item_page.find_text_overview() == Texts.TEXT_OVERVIEW
                and
                pay_item_page.find_summary_info().is_displayed())

    @allure.title('Завершение покупки')
    def test_finish(self, driver, login_page, add_to_cart_page, pay_item_page, finish_page):
        login_page.full_login()
        add_to_cart_page.full_add_item_to_cart()
        pay_item_page.full_pay_item()
        finish_page.find_and_click_finish_button()
        assert ((finish_page.find_text_thanks() == Texts.TEXT_THANKS)
                and
                (finish_page.find_text_checkout_complete() == Texts.TEXT_COMPLETE))
