import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.login.login_props import LoginProperties
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(LoginProperties):

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    def login_page(self,email,pwd):

        login_home=self.home_login
        login_home.click()

        email_ad=self.wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Email']")))
        email_ad.click()
        email_ad.send_keys(email)

        password=self.password_input
        password.click()
        password.send_keys(pwd)

        login_button=self.login_click
        login_button.click()


