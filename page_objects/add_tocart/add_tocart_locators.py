from selenium.webdriver.common.by import By


class AddToCartLocators(object):
    ADD_BUTTON=(By.XPATH,"//div[3]//div[1]//div[1]//div[6]//div[1]//div[2]//a[1]")
    ADD_ITEM=(By.XPATH,"//i[@class='icon-add']")
    ITEM_NAME=(By.XPATH,"//h4[normalize-space(text())='Chicken C Mo:Mo']")
    ITEM_PRICE=(By.XPATH,"//div[3]//div[1]//div[1]//div[6]//div[1]//div[1]//p[1]")

