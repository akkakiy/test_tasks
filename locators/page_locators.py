from selenium.webdriver.common.by import By


class LocatorsMainPage:

    # логотип магазина
    LOGO = (By.XPATH, "//div[contains(text(),'Swag Labs')]")
    # поле ввода имени пользователя
    USERNAME = (By.XPATH, "//input[@id='user-name']")
    # поле ввода пароля
    PASSWORD = (By.XPATH, "//input[@id='password']")
    # кнопка входа
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
    # текст названия товара
    PRODUCTS = (By.XPATH, "//span[contains(text(),'Products')]")
    # ссылка на страницу продукта
    PRODUCT = (By.XPATH, "//div[normalize-space()='Sauce Labs Backpack']")
    # кнопка добавления в корзину
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@id='add-to-cart']")
    # кнопка корзины
    BASKET_BUTTON = (By.XPATH, "//a[@class='shopping_cart_link']")
    # текст корзины
    TEXT_BASKET = (By.XPATH, "//span[@class='title']")
    # текст названия товара в корзине
    ITEM_NAME = (By.XPATH, "//div[@class='inventory_item_name']")
    # текст цены товара в корзине
    ITEM_PRICE = (By.XPATH, "//div[@class='inventory_item_price']")
    # кнопка перехода к оформлению
    CHECKOUT_BUTTON = (By.XPATH, "//button[@id='checkout']")
    # поле ввода имени
    FIRST_NAME_FIELD = (By.XPATH, "//input[@id='first-name']")
    # поле ввода фамилии
    LAST_NAME_FIELD = (By.XPATH, "//input[@id='last-name']")
    # поле ввода почты
    ZIP_POSTAL_CODE_FIELD = (By.XPATH, "//input[@id='postal-code']")
    # кнопка продолжения
    CONTINUE_BUTTON = (By.XPATH, "//input[@id='continue']")
    # текст подтверждения оформления
    TEXT_FINISHED = (By.XPATH, "//span[contains(text(),'Checkout: Overview')]")
    # информация о заказе
    SUMMARY_INFO = (By.XPATH, "//div[@class='summary_info']")
    # кнопка завершения покупки
    FINISH_BUTTON = (By.XPATH, "//button[@id='finish']")
    # текст завершения покупки
    CHECKOUT_COMPLETE = (By.XPATH, "//span[@class='title']")
    # текст "Thank you for your order!"
    THANKS = (By.XPATH, "//h2[normalize-space()='Thank you for your order!']")
    # кнопка "Back Home"
    BACK_HOME_BUTTON = (By.XPATH, "//button[@id='back-to-products']")








