import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Запуск Firefox; убедитесь, что geckodriver в PATH
    service = FirefoxService()
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_checkout_total_amount(driver):
    wait = WebDriverWait(driver, 10)

    # 1. Открыть сайт
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизоваться как standard_user
    wait.until(
        EC.visibility_of_element_located(
            (
                By.ID, "user-name"
            )
        )
    ).send_keys("standard_user")
    wait.until(
        EC.visibility_of_element_located(
            (
                By.ID, "password"
            )
        )
    ).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    # 3. Добавить в корзину три товара
    # Список локаторов кнопок Add to cart
    products_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]
    for btn_id in products_to_add:
        wait.until(EC.element_to_be_clickable((By.ID, btn_id))).click()

    # 4. Перейти в корзину
    wait.until(
        EC.element_to_be_clickable(
            (
                By.CLASS_NAME, "shopping_cart_link"
            )
        )
    ).click()

    # 5. Нажать Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # 6. Заполнить форму данными
    wait.until(
        EC.visibility_of_element_located(
            (
                By.ID, "first-name"
            )
        )
    ).send_keys("Иван")
    wait.until(
        EC.visibility_of_element_located(
            (
                By.ID, "last-name"
            )
        )
    ).send_keys("Иванов")
    wait.until(
        EC.visibility_of_element_located(
            (
                By.ID, "postal-code"
            )
        )
    ).send_keys("123456")
    wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    # 7. Считать итоговую стоимость (Total)
    total_locator = (By.CLASS_NAME, "summary_total_label")
    total_text = wait.until(
        EC.visibility_of_element_located(
            total_locator
        )
    ).text
    # пример строки: "Total: $58.29"

    # 8. Проверить, что сумма равна $58.29
    assert "58.29" in total_text, (
        f"Ожидали сумму $58.29, получили: {total_text}"
    )
