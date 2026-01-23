from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.feature("Инвентарь")
class InventoryPage:
    """
    Страница списка товаров.

    Атрибуты:
        driver (WebDriver): Экземпляр драйвера Selenium.
        wait (WebDriverWait): Объект ожидания.
    """

    def __init__(self, driver):
        """
        Инициализация страницы инвентаря.

        :param driver: WebDriver — экземпляр драйвера Selenium.
        Тип: webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.title("Добавить товар в корзину")
    @allure.description("Кликает по кнопке добавления товара по его ID.")
    def add_product_to_cart(self, product_id):
        """
        Добавляет продукт в корзину по его идентификатору.

        :param product_id: str — ID продукта, кнопки добавления.
        :return: None
        """
        with allure.step(f"Добавить продукт с ID '{product_id}' в корзину"):
            self.wait.until(
                EC.element_to_be_clickable((By.ID, product_id))
            ).click()

    @allure.title("Перейти в корзину")
    @allure.description(
        "Переходит на страницу корзины, кликнув по ссылке или иконке корзины."
    )
    def go_to_cart(self):
        """
        Переходит на страницу корзины.

        :return: None
        """
        with allure.step("Перейти в корзину"):
            self.wait.until(
                EC.element_to_be_clickable(
                    (
                        By.CLASS_NAME, "shopping_cart_link"
                    )
                )
            ).click()
