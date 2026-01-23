from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.feature("Калькулятор с задержкой")
class SlowCalculatorPage:
    """
    Страница с калькулятором, у которого есть задержка.

    Атрибуты:
        driver (WebDriver): Экземпляр драйвера Selenium.
        wait (WebDriverWait): Объект ожидания.
        delay_input_locator (tuple): Локатор для поля задержки.
        result_locator (tuple): Локатор для области с результатом.
    """

    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.

        :param driver: WebDriver — экземпляр драйвера Selenium.
        Тип: webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        # Локаторы элементов
        self.delay_input_locator = (By.CSS_SELECTOR, "#delay")
        self.result_locator = (By.XPATH, "//div[@class='screen']")

    @allure.title("Открыть страницу калькулятора")
    @allure.description("Открывает страницу по указанному URL.")
    def open(self, url):
        """
        Открывает страницу по URL.

        :param url: str — URL страницы.
        :return: None
        """
        with allure.step(f"Открыть страницу по URL: {url}"):
            self.driver.get(url)

    @allure.title("Установить задержку")
    @allure.description("Устанавливает значение задержки в поле ввода.")
    def set_delay(self, value):
        """
        Устанавливает задержку в поле ввода.

        :param value: str — значение задержки в виде строки.
        :return: None
        """
        with allure.step(f"Установить задержку: {value}"):
            delay_input = self.wait.until(
                EC.element_to_be_clickable(self.delay_input_locator)
            )
            delay_input.clear()
            delay_input.send_keys(value)

    @allure.title("Нажать кнопку с текстом")
    @allure.description("Ищет кнопку по тексту и классу, кликает по ней.")
    def click_button_by_text(self, text, class_name):
        """
        Общий метод для клика по кнопкам по тексту и классу.

        :param text: str — текст на кнопке.
        :param class_name: str — часть класса кнопки.
        :return: None
        """
        xpath_expr = (
            f"//span[contains(@class, '{class_name}') and text()='{text}']"
        )
        with allure.step(
            f"Кликнуть по кнопке с текстом '{text}' и классом '{class_name}'"
        ):
            button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, xpath_expr))
            )
            button.click()

    @allure.title("Получить результат")
    @allure.description(
        "Ждет, пока результат не станет равен '15',"
        " возвращает текст результата."
    )
    def get_result(self):
        """
        Получает текст результата, ожидая его появления.

        :return: str — текст результата.
        """
        # ждем 45 секунд, пока текст не станет равен "15"
        wait = WebDriverWait(self.driver, 45)
        result_locator = (By.XPATH, "//div[@class='screen']")
        wait.until(lambda d: d.find_element(*result_locator).text == "15")
        # возвращает текст элемента результата
        result_element = self.wait.until(
            EC.presence_of_element_located(self.result_locator)
        )
        return result_element.text
