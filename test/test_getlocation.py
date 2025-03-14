import logging
import time

from get_location.getlocation_page import GetLocationPage
from login.login_page import LoginPage
from setup.base_test import BaseTest


class TestGetLocation(BaseTest):
    def test_login_first(self):
        url = self.cred["base_url"]
        self.driver.get(url)
        logging.info("driver initiliazed")
        email=self.cred['email']
        logging.info("get email successfull")
        password=self.cred['password']
        logging.info("get password successfull")
        login=LoginPage(self.driver)
        login.login_page(email,password)
        getlocation_p=GetLocationPage(self.driver)
        getlocation_p.getlocation_page()
        logging.info("product page")
        time.sleep(10)







