from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time
load_dotenv()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
class Linkedin:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10000)
        self.login()
    def login(self):
        
        self.driver.get("https://www.linkedin.com/")

        username_element = self.driver.find_element(By.ID, "session_key")
        password_element = self.driver.find_element(By.ID, "session_password")

        username_element.send_keys(USERNAME)
        password_element.send_keys(PASSWORD)
        password_element.submit()
    def make_post(self, message):
        
        start_post_button = self.driver.find_element(By.ID, "ember29")
        start_post_button.click()
        text_field = self.driver.find_element(By.CSS_SELECTOR, ".ql-editor[data-placeholder='What do you want to talk about?']")
        text_field.send_keys(message)
        time.sleep(2) #this should probably not be here lol, rip if it takes longer than 2 seconds for the post button to become enabled. 
        buttons = self.driver.find_elements(By.CSS_SELECTOR, "button.share-actions__primary-action")
        submit_button = buttons[0]        
        submit_button.click()
linkedin_instance = Linkedin()
linkedin_instance.make_post("hello world!")