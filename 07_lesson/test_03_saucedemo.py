import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    service = FirefoxService()
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_checkout_total_amount(driver):
    # 1. Открываем сайт
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")

    # 2. Авторизация
    login_page.login("standard_user", "secret_sauce")

    # 3. Добавляем товары
    inventory_page = InventoryPage(driver)
    products_ids = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]
    for pid in products_ids:
        inventory_page.add_product_to_cart(pid)

    # 4. Переходим в корзину
    inventory_page.go_to_cart()

    # 5. Нажимаем checkout
    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    # 6. Заполняем форму оформления заказа
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_personal_info("Иван", "Иванов", "123456")
    checkout_page.continue_checkout()

    # 7. Получаем итоговую сумму
    total_text = checkout_page.get_total()
    print("Total:", total_text)

    # 8. Проверка суммы
    assert "58.29" in total_text, (
        f"Ожидали сумму 58.29, а получили: {total_text}"
    )
