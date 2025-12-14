import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class StringUtils:
    @staticmethod
    def add_period(text: str) -> str:
        if not isinstance(text, str):
            raise TypeError("text must be a str")
        if not text:
            return "."
        if not text.endswith('.'):
            text += '.'
        return text

    @staticmethod
    def replace_spaces(text: str, char: str = "_") -> str:
        if not isinstance(text, str):
            raise TypeError("text must be a str")
        if not text:
            return ""
        return text.replace(" ", char)


@pytest.fixture
def driver():
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)
    driver.implicitly_wait(15)
    yield driver
    driver.quit()


def test_form_submission(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

    driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys(
        "Иван")
    driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys(
        "Петров")
    driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys(
        "Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys(
        "test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys(
        "+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").send_keys(
        "")  # проверьте правильность селектора
    driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys(
        "Москва")
    driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys(
        "Россия")
    driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys(
        "QA")
    driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys(
        "SkyPro")

    # Нажимаем кнопку Submit
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Функция для получения цвета рамки
    def get_border_color(element):
        return element.value_of_css_property("border-color")

    # Функция для проверки, что цвет строго равен rgb(245, 194, 199)
    def is_exact_color(rgb_string):
        target_rgb = (245, 194, 199)
        rgb_string = rgb_string.strip().lower()
        # Проверяем, что строка начинается с 'rgb(' и заканчивается на ')'
        if rgb_string.startswith("rgb(") and rgb_string.endswith(")"):
            # Вырезаем содержимое внутри скобок
            inner = rgb_string[4:-1]
        # Разделяем по запятой
        parts = inner.split(",")
        if len(parts) == 3:
            try:
                r = int(parts[0].strip())
                g = int(parts[1].strip())
                b = int(parts[2].strip())
                print(f"Parsed colors: R={r}, G={g}, B={b}")
                return (r, g, b) == target_rgb
            except ValueError:
                print("Не удалось преобразовать значения в числа.")
                return False
        print("Строка не в ожидаемом формате:", rgb_string)
        return False
        # Проверка
        zip_code_elem = driver.find_element(By.ID, "zip-code")
        zip_border_color = get_border_color(zip_code_elem)
        assert is_exact_color(zip_border_color), \
            (
             f"Zip code должно быть подсвечено точно цветом"
             f"rgb(245, 194, 199),получено: {zip_border_color}"
             )

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "company": "SkyPro"
    }

    def is_green_shade(rgb_string):
        # парсим строку
        if rgb_string.startswith("rgb(") and rgb_string.endswith(")"):
            inner = rgb_string[4:-1]
        parts = inner.split(",")
        if len(parts) == 3:
            try:
                r = int(parts[0].strip())
                g = int(parts[1].strip())
                b = int(parts[2].strip())
                # Проверяем, что G значительно больше R и B
                return g > r + 20 and g > b + 20 and r < 200 and b < 200
            except ValueError:
                return False
    return False
    for field_id, value in fields.items():
        elem = driver.find_element(By.ID, field_id)
        color = get_border_color(elem).replace(" ", "")
        assert is_green_shade(color), \
            (
                f"Поле {field_id} должно быть подсвечено зеленым,"
                f" текущий цвет: {color}"
            )
