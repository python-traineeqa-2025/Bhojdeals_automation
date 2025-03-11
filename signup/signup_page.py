from signup.signup_properties import SignUpProperties


class SignUpPage(SignUpProperties):
    def __init__(self,driver):
        self.driver=driver
        self.dropdown = None

    def signup_page(self,uname,email_id,pwd,confirm_pwd,phone):

        choose_signup=self.signup_options
        choose_signup.click()

        name=self.name_input
        name.click()
        name.send_keys(uname)

        email=self.email_input
        email.click()
        email.send_keys(email_id)

        password= self.password_input
        password.click()
        password.send_keys(pwd)

        confirm_password = self.confirm_password_input
        confirm_password.click()
        confirm_password.send_keys(confirm_pwd)

        mobile_number = self.mobilenumber_input
        mobile_number.click()
        mobile_number.send_keys(phone)

        checkbox=self.term_condtion_checkbox
        checkbox.click()


        signup=self.signup_click
        signup.click()

        dropdown=self.dropdown_country
        dropdown.click()

    i = 0
    while i < len(dropdown):
        if (dropdown[i].text == "Nepal"):
            dropdown[i].click()
        i = i + 1









