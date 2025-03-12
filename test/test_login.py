import logging
import time

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from login.login_page import LoginPage
from setup.base_test import BaseTest
from selenium.webdriver.support import expected_conditions as EC


class TestLogin(BaseTest):
    def test_login(self):
        url = self.cred["base_url"]
        self.driver.get(url)
        logging.info("driver initialized")

        loginpage=LoginPage(self.driver)
        email=self.cred["email"]
        logging.info("Email entered")

        pwd=self.cred["password"]
        logging.info("Password entered")
        loginpage.login_page(email,pwd)
        time.sleep(10)


