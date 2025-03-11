from signup.signup_locators import SignUpLocators


class SignUpProperties(SignUpLocators):

    @property
    def signup_options(self):
        return self.driver.find_element(*SignUpLocators.SIGNUP_OPTIONS)

    @property
    def name_input(self):
        return self.driver.find_element(*SignUpLocators.NAME)

    @property
    def email_input(self):
        return self.driver.find_element(*SignUpLocators.EMAIL)

    @property
    def password_input(self):
        return self.driver.find_element(*SignUpLocators.PASSWORD)

    @property
    def confirm_password_input(self):
        return self.driver.find_element(*SignUpLocators.CONFIRM_PASSWORD)

    @property
    def mobilenumber_input(self):
        return self.driver.find_element(*SignUpLocators.MOBILE_NUMBER)

    @property
    def term_condtion_checkbox(self):
        return self.driver.find_element(*SignUpLocators.TERMS_CONDITIONS)

    @property
    def signup_click(self):
        return self.driver.find_element(*SignUpLocators.SIGN_UP)

    @property
    def dropdown_country(self):
        return self.driver.find_elements(*SignUpLocators.COUNTRY_DROPDOWN)

