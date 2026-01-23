from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class FormPage:
    """
    Страница формы для автоматизированного тестирования.

    Атрибуты:
        driver (WebDriver): экземпляр драйвера Selenium.
        wait (WebDriverWait): объект WebDriverWait для ожиданий.
        fields (dict): словарь полей формы и значений для заполнения.
    """

    def __init__(self, driver):
        """
        Инициализация страницы формы.

        :param driver: WebDriver — экземпляр драйвера Selenium.
        Тип: webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    @allure.title("Открыть страницу формы")
    @allure.description("Переход на страницу формы для заполнения данных.")
    def open(self):
        """
        Открывает страницу формы в браузере.

        :return: None
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    @allure.title("Заполнить форму данными")
    @allure.description(
        "Заполняет все поля формы данными из атрибута self.fields."
        )
    def fill_form(self):
        """
        Заполняет все поля формы указанными значениями.

        :return: None
        """
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((By.NAME, field))
            ).send_keys(value)

    @allure.title("Отправить форму")
    @allure.description("Кликает по кнопке отправки формы.")
    def submit_form(self):
        """
        Отправляет заполненную форму.

        :return: None
        """
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]'))
        ).click()

    @allure.title("Получить класс элемента поля")
    @allure.description(
        "Возвращает значение атрибута class у элемента по идентификатору."
        )
    def get_field_class(self, field_id):
        """
        Получает значение атрибута class элемента поля формы.

        :param field_id: str — ID элемента формы.
        :return: str — значение атрибута class.
        """
        element = self.wait.until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        return element.get_attribute("class")

    @allure.title("Проверка ошибки ZIP-кода")
    @allure.description("Проверяет наличие ошибки в поле ZIP-кода по классу.")
    def check_zip_code_error(self):
        """
        Проверяет,
        есть ли ошибка в поле ZIP-кода по наличию класса 'alert-danger'.

        :return: bool — True, если есть ошибка; False — если нет.
        """
        class_value = self.get_field_class("zip-code")
        return "alert-danger" in class_value

    @allure.title("Проверка успешных выделений полей")
    @allure.description(
        "Проверяет, что все поля прошли валидацию и имеют класс 'success'."
        )
    def check_fields_success(self):
        """
        Проверяет, что указанные поля имеют класс 'success',
        что означает успешную валидацию.

        :return: bool — True, если все поля успешны;
        False — если хотя бы одно не прошло.
        """
        fields = [
            'first-name', 'last-name', 'address', 'e-mail', 'phone',
            'city', 'country', 'job-position', 'company'
        ]
        for field in fields:
            class_value = self.get_field_class(field)
            if "success" not in class_value:
                return False
        return True

    @allure.title("Проверка состояния формы после отправки")
    @allure.description(
        "Проверяет,"
        "что ZIP-код имеет ошибку и остальные поля успешно прошли проверку."
        )
    def check_form_submission(self):
        """
        Выполняет проверки состояния формы после отправки.

        :raises AssertionError: если проверки не прошли.
        """
        with allure.step("Проверить наличие ошибки в ZIP-коде"):
            assert self.check_zip_code_error(), (
                "Значение ZIP-кода не вызывает ошибку."
            )

        with allure.step(
            "Проверить, что все остальные поля успешно прошли проверку"
        ):
            assert self.check_fields_success(), (
                "Некоторые поля не прошли валидацию успешно."
                )
