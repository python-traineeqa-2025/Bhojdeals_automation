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
            logging.info("login button clicked")

            email = credentials['email']
            logging.info(email)

            pwd = credentials['pwd']
            logging.info(pwd)

            login.login_page(email,pwd)
            invalid_message_email = self.driver.find_element(By.XPATH, "//span[@class='invalid-message']")

            try:
                if invalid_message_email:
                    logging.info({invalid_message_email.text})
                else:
                    invalid_message_password = self.driver.find_element(By.XPATH, "//div[@role='alert']")
                    logging.info({invalid_message_password.text})

            except NoSuchElementException:
                print("The error message doesnot exist")
            finally:
                time.sleep(10)
                self.driver.back()












# import json
# import logging
# import time
# import pytest
# from selenium.webdriver.common.by import By
#
# from page_objects.login.login_page import LoginPage
# from setup.base_test import BaseTest
#
#
# def load_credentials():
#     cred_path = r"C:\Users\anushagi\OneDrive - Infinite Computer Solutions (India) Limited\Documents\Bhojdeals_automation\creds\cred_valid_invalid.json"
#     with open(cred_path, 'r') as file:
#         cred = json.load(file)
#
#     # Convert JSON data to a list of tuples: (test_case_name, email, password)
#     return [(test_case, details['email'], details['pwd']) for test_case, details in cred.items()]
#
#
# class TestValidInvalid(BaseTest):
#
#     @pytest.mark.parametrize("test_case, email, password", load_credentials())
#     def test_valid_invalid(self, test_case, email, password):
#         """Parameterized test for login functionality with different credentials."""
#         invalid_message=self.driver.find_element(By.XPATH,"//span[@class='invalid-message']")
#         url = self.cred["base_url"]
#         self.driver.get(url)
#         time.sleep(3)
#
#         login = LoginPage(self.driver)
#
#         logging.info(f"Running test: {test_case}")
#         logging.info({invalid_message.text})
#         logging.info(f"Email: {email}")
#         logging.info(f"Password: {password}")
#
#         login.login_page(email, password)
#         time.sleep(5)
#
#         self.driver.back()
#
