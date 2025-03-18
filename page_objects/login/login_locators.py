from selenium.webdriver.common.by import By


class LoginLocators(object):
    HOME_LOGIN=(By.XPATH,"//a[normalize-space()='login']")
    EMAIL=(By.XPATH,"//input[@placeholder='Email']")
    PASSWORD=(By.XPATH,"//input[@placeholder='Password']")
    LOGIN=(By.XPATH,"//button[@type='submit']")
