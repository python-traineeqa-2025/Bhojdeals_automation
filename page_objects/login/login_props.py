from page_objects.login.login_locators import LoginLocators


class LoginProperties(LoginLocators):



    @property
    def home_login(self):
        return self.driver.find_element(*LoginLocators.HOME_LOGIN)


    @property
    def email_input(self):
        return self.driver.find_element(*LoginLocators.EMAIL)

    @property
    def password_input(self):
        return self.driver.find_element(*LoginLocators.PASSWORD)

    @property
    def login_click(self):
        return self.driver.find_element(*LoginLocators.LOGIN)


