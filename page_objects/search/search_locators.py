from selenium.webdriver.common.by import By

class SearchLocators (object):
    SEARCH_BOX = (By.XPATH,"//input[@id='exampleInput1']")
    DROPDOWN = (By.XPATH,"//div[@class= 'main-auto-suggestion']//ul")
    DROPDOWN_ITEMS=(By.XPATH, "//div[@class='main-auto-suggestion']//span")