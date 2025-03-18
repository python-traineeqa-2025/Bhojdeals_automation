import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.login.login_props import LoginProperties
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(LoginProperties):

    def __init__(self,driver):
        self.driver=driver

    def login_page(self,email,pwd):

        login_home=self.home_login
        login_home.click()

        # email_ad=WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((By.ID,"__BVID__76")))
        email_ad=self.email_input
        email_ad.click()
        email_ad.send_keys(email)

        password=self.password_input
        password.click()
        password.send_keys(pwd)

        login_button=self.login_click
        login_button.click()


