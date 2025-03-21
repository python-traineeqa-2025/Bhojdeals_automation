from selenium.webdriver.common.by import By

class SearchLocators (object):
    SEARCH_BOX = (By.XPATH,"//input[@id='exampleInput1']")
    DROPDOWN = (By.XPATH,"//div[@class= 'main-auto-suggestion']//ul")
    DROPDOWN_ITEMS=(By.XPATH, "//div[@class='main-auto-suggestion']//span")
    TODAYS_DEAL=(By.XPATH,"//h2[normalize-space()=\"Today's Deals\"]")
    BROWSER_CATEGORY=(By.XPATH,"//label[@for='Bakery']")
    BROWSER_CUISINE=(By.XPATH,"//label[contains(text(),'Indian')]")
    SORT_POPULARITY=(By.XPATH,"//div[contains(@class,'pr-md-0')]//div/select")
    SORT_PRICE=(By.XPATH,"//div[contains(@class,'col-sm-6 col-md-6 col-xl-3')][2]/div/select")
    ALL_RESTAURANT = (By.XPATH, "//h2[normalize-space()='All Restaurants']")
    RESET=(By.XPATH,"//div[@class='restaurant-cuisines']//h4//button")