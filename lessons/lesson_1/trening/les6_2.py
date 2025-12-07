from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(
ChromeDriverManager().install())) #инициализация драйвера

browser.get("https://rzd.ru/")

browser.title

current_title = browser.title
print(current_title)

browser.quit()