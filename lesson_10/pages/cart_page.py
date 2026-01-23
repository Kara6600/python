from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.feature("Корзина")
class CartPage:
    """
    Страница корзины покупок.

    Атрибуты:
        driver (WebDriver): Экземпляр драйвера Selenium.
        wait (WebDriverWait): Объект ожидания.
    """

    def __init__(self, driver):
        """
        Инициализация страницы корзины.

        :param driver: WebDriver — экземпляр драйвера Selenium.
        Тип: webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.title("Переход к оформлению заказа")
    @allure.description("Кликает по кнопке 'Перейти к оформлению заказа'.")
    def proceed_to_checkout(self):
        """
        Выполняет клик по кнопке перехода к оформлению заказа.

        :return: None
        """
        with allure.step("Нажать кнопку 'Перейти к оформлению заказа'"):
            self.wait.until(
                EC.element_to_be_clickable((By.ID, "checkout"))
            ).click()
