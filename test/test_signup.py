import time

from setup.base_test import BaseTest
from signup.signup_page import SignUpPage


class TestSignup(BaseTest):

    def test_signup(self):
        url=self.cred["base_url"]
        self.driver.get(url)
        signuppage=SignUpPage(self.driver)
        uname=self.cred["name"]
        email_id=self.cred["email"]
        pwd = self.cred["password"]
        confirm_pwd = self.cred["password"]
        phone= self.cred["mobile_number"]
        # drop_down=self.dropdown
        signuppage.signup_page(uname,email_id,pwd,confirm_pwd,phone)
        time.sleep(10)










