from selenium.webdriver.common.by import By


class GetFoodLocators(object):

    GETFOOD=(By.XPATH,"//h2[normalize-space()='Get Food & Grocery delivered']")
    LOCATION_KTM_PATAN=(By.XPATH,"//img[@title='Kathmandu and Lalitpur']")
    LOCATION_BHAKTAPUR=(By.XPATH,"//img[@title='Bhaktapur']")
    # GETFOOD=(By.XPATH,"//div[@class='border-right col-xl-6 col-6']//a[@href='#']//span//img[@alt='Get Food Delivered']")
    # GETFOOD=(By.XPATH,"//div[@class='border-right col-xl-6 col-6']//a[@href='#']//span//img[@alt='Get Food Delivered']")
