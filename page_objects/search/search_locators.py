from selenium.webdriver.common.by import By

class SearchLocators (object):
    SEARCH_BOX = (By.XPATH,"//input[@id='exampleInput1']")
    DROPDOWN = (By.XPATH,"//div[@class= 'main-auto-suggestion']//ul")
    DROPDOWN_ITEMS=(By.XPATH, "//div[@class='main-auto-suggestion']//span")
    TODAYS_DEAL=(By.XPATH,"//h2[normalize-space()=\"Today's Deals\"]")
    BROWSER_CATEGORY=(By.XPATH,"//label[@for='Bakery']")
    BROWSER_CUISINE=(By.XPATH,"//label[contains(text(),'Indian')]")
    SORT_POPULARITY=(By.XPATH,"")