
import json
import logging
import time
import pytest

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from page_objects.login.login_page import LoginPage
from setup.base_test import BaseTest

cred_path = r"C:\Users\anushagi\OneDrive - Infinite Computer Solutions (India) Limited\Documents\Bhojdeals_automation\creds\cred_valid_invalid.json"
with open(cred_path, 'r') as file:
    credentials_data = json.load(file)

test_data = [(cred["email"], cred["pwd"]) for cred in credentials_data.values()]


class TestValidInvalidPara(BaseTest):

    @pytest.mark.parametrize("email, pwd", test_data)
    def test_valid_invalid(self, email, pwd):
        url = self.cred["base_url"]
        self.driver.get(url)

        login = LoginPage(self.driver)

        logging.info(f"Testing with Email: {email} and Password: {pwd}")

        login.login_page(email, pwd)
        logging.info("Login button clicked")

        time.sleep(5)

        try:
            invalid_message_email = self.driver.find_element(By.XPATH, "//span[@class='invalid-message']")
            logging.info(f"Invalid Message Displayed: {invalid_message_email.text}")
        except NoSuchElementException:
            logging.info("Password or email is incorrect")
        finally:
            time.sleep(3)
            self.driver.back()
