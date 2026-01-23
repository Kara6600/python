import pytest
import allure
from selenium import webdriver
from pages.FormPage import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Форма обратной связи")
@allure.title("Проверка успешной отправки формы")
@allure.description(
    "Тест заполняет форму, отправляет её и проверяет подтверждение."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission_flow(driver):
    with allure.step("Создание объекта страницы формы"):
        form_page = FormPage(driver)
    with allure.step("Открытие страницы формы"):
        form_page.open()
    with allure.step("Заполнение формы"):
        form_page.fill_form()
    with allure.step("Отправка формы"):
        form_page.submit_form()
    with allure.step("Проверка успешной отправки формы"):
        form_page.check_form_submission()
