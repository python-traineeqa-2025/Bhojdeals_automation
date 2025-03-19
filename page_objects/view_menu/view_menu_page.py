from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.view_menu.view_menu_props import ViewMenuPropertries


class ViewMenuPage(ViewMenuPropertries):

    def __init__(self, driver):
        self.driver = driver
        self.wait=WebDriverWait(self.driver, 10)


    def view_menu_page(self):
        view=self.select_restaurant
        view.click()
        self.driver.execute_script('scrollBy(0,1000)')

        # parent=self.driver.find_element(By.XPATH,'//div[contains(@class,"category-tab")]//div[@class="nav"]')
        # view_cat=parent.find_element(By.XPATH,'///li//a[text()="Mo:Mo')
        view_category=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Mo:Mo']")))
        view_category.click()








