from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Создаем экземпляр браузера Chrome
driver = webdriver.Chrome()

try:
    # Переходим на страницу
    driver.get("http://uitestingplayground.com/dynamicid")
    
    # Находим синюю кнопку
    # Обычно, она имеет класс btn-primary или уникальный ID
    # Попробуем по CSS селектору класса
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    
    # Нажимаем на кнопку
    blue_button.click()
    
    # Чтобы убедиться, что все сработало, делаем небольшую задержку
    time.sleep(1)

finally:
    # Закрываем браузер
    driver.quit()