from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Инициализация драйвера (например, Chrome)
driver = webdriver.Chrome()

# Переход на сайт
driver.get("http://uitestingplayground.com/visibility")

# Проверка видимости кнопки Opacity 0
is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()

print(is_displayed)  # Вывод статуса видимости Opacity 0

# Нажатие на кнопку Hide
driver.find_element(By.CSS_SELECTOR, "#hideButton").click()
sleep(2)

# Еще раз проверим видимость
is_displayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed()
print(is_displayed)  # Еще раз выводим статус видимости Opacity 0

sleep(2)

# Закрываем браузер
driver.quit()