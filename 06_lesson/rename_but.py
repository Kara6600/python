from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Переходим на страницу
    driver.get("http://uitestingplayground.com/textinput")

    # Находим поле ввода и вводим текст "SkyPro"
    input_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "newButtonName"))
    )
    input_field.clear()
    input_field.send_keys("SkyPro")

    # Находим синюю кнопку и нажимаем на нее
    blue_button = driver.find_element(By.ID, "updatingButton")
    blue_button.click()

    # Получаем обновленный текст кнопки
    updated_text = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )
    # Теперь выводим текст кнопки в консоль
    button_text = driver.find_element(By.ID, "updatingButton").text
    print(button_text)  # Ожидаемый вывод: "SkyPro"

finally:
    driver.quit()
