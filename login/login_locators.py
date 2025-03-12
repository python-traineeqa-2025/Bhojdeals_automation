from selenium.webdriver.common.by import By


class LoginLocators(object):
    HOME_LOGIN=(By.XPATH,"//a[normalize-space()='login']")
    EMAIL=(By.ID,"__BVID__76")
    PASSWORD=(By.ID,"__BVID__77")
    LOGIN=(By.XPATH,"//button[@type='submit']")
