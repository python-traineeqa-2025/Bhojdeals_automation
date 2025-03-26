import json
import logging
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from page_objects.login.login_page import LoginPage
from setup.base_test import BaseTest


class TestValidInvalid(BaseTest):

    def test_valid_invalid(self):
        url = self.cred["base_url"]
        self.driver.get(url)
        cred_path = r"C:\Users\anushagi\OneDrive - Infinite Computer Solutions (India) Limited\Documents\Bhojdeals_automation\creds\cred_valid_invalid.json"
        with open(cred_path, 'r') as file:
            cred = json.load(file)
        time.sleep(5)

        for type,credentials in cred.items():
            login = LoginPage(self.driver)
            email = credentials['email']
            pwd = credentials['pwd']
            logging.info(f"Testing with Email: {email} and Password: {pwd}")
            login.login_page(email,pwd)
            logging.info("login button clicked")

            try:
                invalid_message_email = self.driver.find_element(By.XPATH, "//span[@class='invalid-message']")
                logging.info(invalid_message_email.text)

            except NoSuchElementException:
                logging.info("Password or email is incorrect")
            finally:
                time.sleep(10)
                self.driver.back()











