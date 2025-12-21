import pytest
from selenium import webdriver
from pages.slow_calculator_page import SlowCalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator_with_delay(driver):
    calculator = SlowCalculatorPage(driver)
    calculator.open(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    # Установка задержки 45
    calculator.set_delay("45")

    # Выполнение выражения 7 + 8 =
    calculator.click_button_by_text("7", "btn btn-outline-primary")
    calculator.click_button_by_text("+", "operator btn btn-outline-success")
    calculator.click_button_by_text("8", "btn btn-outline-primary")
    calculator.click_button_by_text("=", "btn btn-outline-warning")

    # Проверка результата 15
    result = calculator.get_result()
    assert result == "15", f"Ожидался результат 15, получено {result}"
