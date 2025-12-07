from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")

    # Нажимаем на синюю кнопку
    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ajaxButton"))
    )
    blue_button.click()

    # Ждем появления зеленой плашки с текстом
    green_msg = WebDriverWait(driver, 16).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )

    # Получаем и выводим текст в консоль
    print(green_msg.text)  # ожидается: "Data loaded with AJAX get request."

finally:
    driver.quit()
