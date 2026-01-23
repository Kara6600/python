from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.feature("Авторизация")
class LoginPage:
    """
    Страница входа в систему.

    Атрибуты:
        driver (WebDriver): Экземпляр драйвера Selenium.
    """

    def __init__(self, driver):
        """
        Инициализация страницы входа.

        :param driver: WebDriver — экземпляр драйвера Selenium.
          Тип: webdriver.WebDriver
        """
        self.driver = driver

    @allure.title("Открыть страницу")
    @allure.description("Открывает страницу по заданному URL.")
    def open(self, url):
        """
        Открывает страницу по URL.

        :param url: str — URL страницы.
        :return: None
        """
        with allure.step(f"Открыть страницу по URL: {url}"):
            self.driver.get(url)

    @allure.title("Войти в систему")
    @allure.description(
        "Вводит имя пользователя и пароль, затем кликает кнопку входа."
        )
    def login(self, username, password):
        """
        Выполняет вход пользователя.

        :param username: str — Имя пользователя.
        :param password: str — Пароль.
        :return: None
        """
        wait = WebDriverWait(self.driver, 10)
        with allure.step(f"Ввести имя пользователя: {username}"):
            wait.until(
                EC.visibility_of_element_located((By.ID, "user-name"))
            ).send_keys(username)
        with allure.step("Ввести пароль"):
            wait.until(
                EC.visibility_of_element_located((By.ID, "password"))
            ).send_keys(password)
        with allure.step("Нажать кнопку входа"):
            wait.until(
                EC.element_to_be_clickable((By.ID, "login-button"))
            ).click()
