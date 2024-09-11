# Тестовый сценарий на покупку товара с сайта "https://www.saucedemo.com/"


## Файлы
    - locators/page_locators.py   -   файл с локаторами используемыми в сценарии

    - page_object/   -   каталог с файлами методов
        - page_object/base_page.py   -   файл с базовыми методами
        - page_object/login_page.py   -   файл с методами работы с магазином
    - tests/   -   каталог с тестами
        - tests/test_login_and_pay.py   -   файл с проверками магазина
        
        - tests/conftest.py   -   файл с фикстурами


    - data.py   -   файл с постоянными используемыми в проверках
    - help.py   -   вспомогательные методы используемые в проверках
    - urls.py   -   файл с адресами страниц
    
    - requirements.txt   -   файл с зависимостями


## Перед работой необходимо установить зависимости

    pip install -r requirements.txt

## Запустить тесты
    
    pytest tests --alluredir=allure_results

## Посмотреть отчет

    allure serve allure_results