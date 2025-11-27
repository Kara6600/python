from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/login")
    
    # Вводим логин
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    # Вводим пароль
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    # Нажимаем кнопку входа
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Ждем появления сообщения
    wait = WebDriverWait(driver, 10)
    try:
        message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )
        print("Найдено сообщение:", message.text)
    except:
        # Если сообщение не появилось
        print("Сообщение не найдено. Проверьте, вошли ли вы успешно или сделайте скриншот страницы.")
        driver.save_screenshot("screenshot.png")
        print("Скриншот сохранен как screenshot.png")
finally:
    driver.quit()