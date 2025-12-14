import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Настройка драйвера Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator_with_delay(driver):
    # Открываем страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
    wait = WebDriverWait(driver, 20)

    # Вводим значение 45 в поле #delay
    delay_input = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay"))
    )
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажимаем кнопку "7"
    wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[@class='btn btn-outline-primary' and text()='7']"
            )
        )
    ).click()
    # Нажимаем "+"
    wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[@class='operator btn btn-outline-success' and"
                "text()='+']"
            )
        )
    ).click()
    # Нажимаем "8"
    wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[@class='btn btn-outline-primary' and"
                "text()='8']"
            )
        )
    ).click()
    # Нажимаем "="
    wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[@class='btn btn-outline-warning' and text()='=']"
            )
        )
    ).click()
    # Ожидаем 45 секунд без sleep()
    wait = WebDriverWait(driver, 45)

    result_locator = (By.XPATH, "//div[@class='screen']")
    wait.until(lambda d: d.find_element(*result_locator).text == "15")
    result_text = wait.until(lambda d: d.find_element(*result_locator).text)
    assert result_text == "15", (
        f"Ожидался результат 15, получено {result_text}"
    )
