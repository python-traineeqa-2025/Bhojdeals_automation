import json
import logging
import time

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
            time.sleep(10)
            self.driver.back()













# import json
# import logging
# import time
# import pytest
#
# from page_objects.login.login_page import LoginPage
# from setup.base_test import BaseTest


# def load_credentials():
#     """Load credentials from JSON file and return as a list of tuples."""
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
#
#         url = self.cred["base_url"]
#         self.driver.get(url)
#         time.sleep(3)
#
#         login = LoginPage(self.driver)
#
#         logging.info(f"Running test: {test_case}")
#         logging.info(f"Email: {email}")
#         logging.info(f"Password: {password}")
#
#         login.login_page(email, password)
#         time.sleep(5)
#
#         self.driver.back()
