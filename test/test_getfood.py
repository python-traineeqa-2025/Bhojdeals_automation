import logging
import time

from getfood.getfood_page import GetFoodPage
from login.login_page import LoginPage
from setup.base_test import BaseTest


class TestGetFood(BaseTest):


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
        getfood_p=GetFoodPage(self.driver)
        getfood_p.getfood_page()
        logging.info("product page")
        time.sleep(10)
    # def test_getFood(self):









    # def test_getfood(self):






