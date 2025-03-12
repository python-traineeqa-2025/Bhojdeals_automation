from selenium.webdriver.common.by import By


class SignUpLocators:
    SIGNUP_HOMEPAGE=(By.XPATH,"//a[normalize-space()='sign up']")
    NAME=(By.XPATH,"//input[@id='inlinefromusername']")
    EMAIL=(By.XPATH,"//input[@id='inlinefromemail']")
    PASSWORD=(By.XPATH,"//input[@id='inlinefrompassword']")
    CONFIRM_PASSWORD=(By.XPATH,"//input[@id='inlinefromconfpassword']")
    MOBILE_NUMBER=(By.XPATH,"//input[@id='inlineFormInputGroup']")
    TERMS_CONDITIONS=(By.XPATH,"//label[@for='termsand']")
    SIGN_UP=(By.XPATH,"//button[@type='submit']")
    COUNTRY_DROPDOWN=(By.ID,'__BVID__84')






