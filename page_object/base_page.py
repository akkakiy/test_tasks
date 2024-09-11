import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получение URL')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Проверка URL')
    def check_url(self, url):
        return WebDriverWait(self.driver, 15).until(EC.url_to_be(url))

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    @allure.step('Поиск и клик по элементу')
    def click_element(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Ввод текста в поле')
    def input_text_in_field(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step('Получение текста из элемента')
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step('Проверка видимости элемента')
    def check_element_visibility(self, locator):
        return self.driver.find_element(locator).is_displayed()

    @allure.step('Ожидание появления элемента')
    def wait_for_closing_of_element(self, locator):
        WebDriverWait(self.driver, 15).until_not(EC.visibility_of_element_located(locator))
