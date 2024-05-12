from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
load_dotenv()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
def login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.linkedin.com/")

    username_element = driver.find_element(By.ID, "session_key")
    password_element = driver.find_element(By.ID, "session_password")

    username_element.send_keys(USERNAME)
    password_element.send_keys(PASSWORD)

    print(driver.page_source);

    password_element.submit()


    driver.quit()

#login()