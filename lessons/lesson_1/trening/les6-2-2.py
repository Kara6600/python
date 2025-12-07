from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(
ChromeDriverManager().install())) #инициализация драйвера

browser.get("http://ya.ru/")
url = browser.current_url
print(url)

browser.quit()