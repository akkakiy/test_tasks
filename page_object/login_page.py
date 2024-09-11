import allure

from help import TestUser, DataUser
from locators.page_locators import LocatorsMainPage
from page_object.base_page import BasePage
from urls import Urls


@allure.suite('Авторизация пользователя')
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверка URL')
    def get_url_catalog(self):
        return self.check_url(Urls.CATALOG_URL)

    @allure.step('Поиск элемента "Username"')
    def find_and_click_username_field(self):
        return self.click_element(LocatorsMainPage.USERNAME)

    @allure.step('Ввод текста в поле "Username"')
    def fill_in_username(self):
        return self.input_text_in_field(LocatorsMainPage.USERNAME, TestUser().test_user()["username"])

    @allure.step('Поиск элемента "Password"')
    def find_and_click_password_field(self):
        return self.click_element(LocatorsMainPage.PASSWORD)

    @allure.step('Ввод текста в поле "Password"')
    def fill_in_password(self):
        return self.input_text_in_field(LocatorsMainPage.PASSWORD, TestUser().test_user()["password"])

    @allure.step('Клик по элементу "Login"')
    def click_login_button(self):
        return self.click_element(LocatorsMainPage.LOGIN_BUTTON)

    @allure.step('Находим текст "Products"')
    def find_text(self):
        return self.get_text(LocatorsMainPage.PRODUCTS)

    @allure.step('Все шаги для авторизации пользователя')
    def full_login(self):
        self.find_and_click_username_field()
        self.fill_in_username()
        self.find_and_click_password_field()
        self.fill_in_password()
        self.click_login_button()


@allure.suite('Добавление товара в корзину')
class AddToCartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Поиск и клик по названию товара')
    def find_and_click_product(self):
        return self.click_element(LocatorsMainPage.PRODUCT)

    @allure.step('Клик по кнопке "Add to cart"')
    def find_and_click_add_to_cart_button(self):
        return self.click_element(LocatorsMainPage.ADD_TO_CART_BUTTON)

    @allure.step('Клик по кнопке "Корзина"')
    def find_and_click_basket_button(self):
        return self.click_element(LocatorsMainPage.BASKET_BUTTON)

    @allure.step('Получение названия товара')
    def find_item_name(self):
        return self.get_text(LocatorsMainPage.ITEM_NAME)

    @allure.step('Получение цены товара')
    def find_item_price(self):
        return self.get_text(LocatorsMainPage.ITEM_PRICE)

    @allure.step('Все шаги для добавления товара в корзину')
    def full_add_item_to_cart(self):
        self.find_and_click_product()
        self.find_and_click_add_to_cart_button()
        self.find_and_click_basket_button()


@allure.suite('Оформление покупки')
class PayItemPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке "Checkout"')
    def find_and_click_checkout_button(self):
        return self.click_element(LocatorsMainPage.CHECKOUT_BUTTON)

    @allure.step('Клик по полю "First Name"')
    def find_and_click_first_name_field(self):
        return self.click_element(LocatorsMainPage.FIRST_NAME_FIELD)

    @allure.step('Ввод текста в поле "First Name"')
    def fill_first_name(self):
        return self.input_text_in_field(LocatorsMainPage.FIRST_NAME_FIELD, DataUser().data_user()["first_name"])

    @allure.step('Клик по полю "Last Name"')
    def find_and_click_last_name_field(self):
        return self.click_element(LocatorsMainPage.LAST_NAME_FIELD)

    @allure.step('Ввод текста в поле "Last Name"')
    def fill_last_name(self):
        return self.input_text_in_field(LocatorsMainPage.LAST_NAME_FIELD, DataUser().data_user()["last_name"])

    @allure.step('Клик по полю "Zip/Postal Code"')
    def find_and_click_zip_postal_code_field(self):
        return self.click_element(LocatorsMainPage.ZIP_POSTAL_CODE_FIELD)

    @allure.step('Ввод текста в поле "Zip/Postal Code"')
    def fill_zip_postal_code(self):
        return self.input_text_in_field(LocatorsMainPage.ZIP_POSTAL_CODE_FIELD, DataUser().data_user()["zip/postal_code"])

    @allure.step('Клик по кнопке "Continue"')
    def find_and_click_continue_button(self):
        return self.click_element(LocatorsMainPage.CONTINUE_BUTTON)

    @allure.step('Получение текста "Checkout: Overview"')
    def find_text_overview(self):
        return self.get_text(LocatorsMainPage.TEXT_FINISHED)

    @allure.step('Получение информации о покупке')
    def find_summary_info(self):
        return self.find_element(LocatorsMainPage.SUMMARY_INFO)

    @allure.step('Все шаги для оформления покупки')
    def full_pay_item(self):
        self.find_and_click_checkout_button()
        self.find_and_click_first_name_field()
        self.fill_first_name()
        self.find_and_click_last_name_field()
        self.fill_last_name()
        self.find_and_click_zip_postal_code_field()
        self.fill_zip_postal_code()
        self.find_and_click_continue_button()
        self.find_text_overview()
        self.find_summary_info()


@allure.suite('Завершение покупки')
class FinishPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке "Finish"')
    def find_and_click_finish_button(self):
        return self.click_element(LocatorsMainPage.FINISH_BUTTON)

    @allure.step('Получение текста "Checkout: Complete!"')
    def find_text_checkout_complete(self):
        return self.get_text(LocatorsMainPage.CHECKOUT_COMPLETE)

    @allure.step('Получение текста "Thank you for your order!"')
    def find_text_thanks(self):
        return self.get_text(LocatorsMainPage.THANKS)

    @allure.step('Клик по кнопке "Back Home"')
    def find_and_click_back_home_button(self):
        return self.click_element(LocatorsMainPage.BACK_HOME_BUTTON)
