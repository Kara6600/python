from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        # Локаторы элементов
        self.delay_input_locator = (By.CSS_SELECTOR, "#delay")
        self.result_locator = (By.XPATH, "//div[@class='screen']")

    def open(self, url):
        self.driver.get(url)

    def set_delay(self, value):
        delay_input = self.wait.until(
            EC.element_to_be_clickable(self.delay_input_locator)
            )
        delay_input.clear()
        delay_input.send_keys(value)

    def click_button_by_text(self, text, class_name):
        """
        Общий метод для клика по кнопкам по тексту и классу
        class_name - это часть класса кнопки,
        например 'btn btn-outline-primary'
        """
        xpath_expr = (
            f"//span[contains(@class, '{class_name}') and text()='{text}']"
        )
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath_expr))
            )
        button.click()

    def get_result(self):
        # ждём 45 сек
        wait = WebDriverWait(self.driver, 45)
        result_locator = (By.XPATH, "//div[@class='screen']")
        wait.until(lambda d: d.find_element(*result_locator).text == "15")
        # Возвращает текст результата
        result_element = self.wait.until(
            EC.presence_of_element_located(self.result_locator)
            )
        return result_element.text
