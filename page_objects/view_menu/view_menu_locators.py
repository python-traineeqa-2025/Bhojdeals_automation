from selenium.webdriver.common.by import By


class ViewMenuLocators(object):
    RESTAURANT=(By.XPATH,"//a/div[contains(@class,'restaurant-type')]")
    MENU_CATEGORY=(By.XPATH,"//div[@class='category-tab col-md-3 col-xl-2']//li[3]//a[1]")