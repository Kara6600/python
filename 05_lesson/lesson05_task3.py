from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Создаем браузер Firefox
driver = webdriver.Firefox()

try:
    # Открываем страницу
    driver.get("http://the-internet.herokuapp.com/inputs")
    
    # Находим поле ввода (по тегу input)
    input_field = driver.find_element(By.TAG_NAME, "input")
    
    # Вводим текст Sky
    input_field.send_keys("Sky")
    time.sleep(0.5)
    
    # Очищаем поле
    input_field.clear()
    time.sleep(0.5)
    
    # Вводим текст Pro
    input_field.send_keys("Pro")
    
    # Можно добавить задержку, чтобы видеть результат
    time.sleep(1)
finally:
    # Закрываем браузер
    driver.quit()
    