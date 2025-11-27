from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Создаем экземпляр браузера Chrome
driver = webdriver.Chrome()

try:
    # Переход на страницу
    driver.get("http://uitestingplayground.com/classattr")
    
    # Найти синюю кнопку по цвету или по другим атрибутам
    # Предположим, что это кнопка с классом btn-primary или ищем по тексту
    # Для надежности используем CSS-селектор, например:
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    
    # Клик по кнопке
    blue_button.click()
    
    # Можно сделать задержку, чтобы убедиться, что все отработало
    time.sleep(1)

finally:
    # Закрыть браузер
    driver.quit()