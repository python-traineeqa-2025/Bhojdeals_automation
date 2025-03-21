import logging
import time

from page_objects.get_location.getlocation_page import GetLocationPage
from page_objects.login.login_page import LoginPage
from setup.base_test import BaseTest


class TestGetLocation(BaseTest):
    def test_get_location(self):
        url = self.cred["base_url"]
        self.driver.get(url)
        logging.info("driver initialized")

        loginpage = LoginPage(self.driver)
        email = self.cred["email"]
        logging.info("Email entered")

        pwd = self.cred["password"]
        logging.info("Password entered")
        loginpage.login_page(email, pwd)
        time.sleep(3)

        getlocation_p=GetLocationPage(self.driver)
        getlocation_p.getlocation_page()
        time.sleep(3)







