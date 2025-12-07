from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

    WebDriverWait(driver, 20).until(
        lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 3
    )

    images = driver.find_elements(By.TAG_NAME, "img")

    WebDriverWait(driver, 10).until(
        lambda d: (
            images[2].get_attribute("src") != ""
            and images[2].get_attribute("src") is not None
        )
    )

    third_image_src = images[2].get_attribute("src")

    print(third_image_src)

finally:
    driver.quit()
