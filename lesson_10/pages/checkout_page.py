from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.feature("Оформление заказа")
class CheckoutPage:
    """
    Страница оформления заказа.

    Атрибуты:
        driver (WebDriver): Экземпляр драйвера Selenium.
        wait (WebDriverWait): Объект ожидания.
    """

    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.

        :param driver: WebDriver — экземпляр драйвера Selenium.
        Тип: webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.title("Заполнить личные данные")
    @allure.description("Заполняет поля фамилии, имени и почтового кода.")
    def fill_personal_info(self, first_name, last_name, postal_code):
        """
        Заполняет поля формы личных данных.

        :param first_name: str — Имя пользователя.
        :param last_name: str — Фамилия пользователя.
        :param postal_code: str — Почтовый код.
        :return: None
        """
        with allure.step("Заполнить имя"):
            self.wait.until(
                EC.visibility_of_element_located((By.ID, "first-name"))
            ).send_keys(first_name)
        with allure.step("Заполнить фамилию"):
            self.wait.until(
                EC.visibility_of_element_located((By.ID, "last-name"))
            ).send_keys(last_name)
        with allure.step("Заполнить почтовый код"):
            self.wait.until(
                EC.visibility_of_element_located((By.ID, "postal-code"))
            ).send_keys(postal_code)

    @allure.title("Продолжить оформление")
    @allure.description(
        "Нажимает кнопку 'Продолжить' для продолжения оформления заказа."
        )
    def continue_checkout(self):
        """
        Нажимает кнопку продолжения.

        :return: None
        """
        with allure.step("Нажать кнопку 'Продолжить'"):
            self.wait.until(
                EC.element_to_be_clickable((By.ID, "continue"))
            ).click()

    @allure.title("Получить сумму заказа")
    @allure.description("Возвращает текст стоимости заказа.")
    def get_total(self):
        """
        Получает сумму заказа из элемента с классом 'summary_total_label'.

        :return: str — текст с общей суммой.
        """
        with allure.step("Извлечь сумму заказа"):
            total_text = self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.CLASS_NAME, "summary_total_label"
                    )
                )
            ).text
        return total_text
