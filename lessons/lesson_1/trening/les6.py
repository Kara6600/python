from time import sleep
from selenium import webdriver

#две строки ниже можно оставить, они не помешают работе
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#три строки ниже - новые, импорт драйвера для Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
browser = webdriver.Firefox(  #поменяли название переменной driver на browser
service=FirefoxService(GeckoDriverManager().install()))

#оставляем предыдущие методы
browser.maximize_window() #для разворачивания окна
browser.get("https://ya.ru/") #для перехода на нужную страницу
sleep(5) #для паузы на загрузку контента страницы
browser.save_screenshot("./ya.png") #для сохранения скриншота
browser.quit() #для закрытия окна