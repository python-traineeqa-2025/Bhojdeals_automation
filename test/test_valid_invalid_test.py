# import json
# import logging
# import time
#
# from page_objects.login.login_page import LoginPage
# from setup.base_test import BaseTest
#
#
# class TestValidInvalid(BaseTest):
#
#     def test_valid_invalid(self):
#         url = self.cred["base_url"]
#         self.driver.get(url)
#         cred_path = r"C:\Users\anushagi\OneDrive - Infinite Computer Solutions (India) Limited\Documents\Bhojdeals_automation\creds\cred_valid_invalid.json"
#         with open(cred_path, 'r') as file:
#             cred = json.load(file)
#
#
#         time.sleep(5)
#
#         for type,credentials in cred.items():
#             login = LoginPage(self.driver)
#             logging.info("login button clicked")
#
#             email = credentials['email']
#             logging.info(email)
#
#             pwd = credentials['pwd']
#             logging.info(pwd)
#
#             login.login_page(email,pwd)
#             time.sleep(10)
#             self.driver.back()
#
#
#
#
#
#
#
#





