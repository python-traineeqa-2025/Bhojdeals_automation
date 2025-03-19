
import logging
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unicodedata import category

from page_objects.search.search_props import SearchProperties

class SearchPage(SearchProperties):
    def __init__(self, driver):
        self.driver = driver #can add webdriver wait here so that there's no need to initialize it everytime

    def search_page(self,food,excepted=None): #can be named search_item
        searchbox = self.search_input
        searchbox.click()
        searchbox.send_keys(food)
        # searchbox.send_keys("amore pizza")
        searchbox.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "main-auto-suggestion"))
        )

        dropdown_item = self.dropdown_items
        # if excepted:
        for item in dropdown_item:

            logging.info(f"Found: {item.text}")
            if excepted:
                if item.text.strip() == excepted:
                    # if item.text.strip() == "Amore Pizza (Koteshwor)":
                    logging.info(f"{item.text.strip()} item matches with expected {excepted}")
                    item.click()
                    break

    def invalid_search(self): #why is this called invalid search
        searchbox = self.search_input
        searchbox.click()
        searchbox.send_keys("pizz")
        searchbox.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME,"main-auto-suggestion")) #since this locator is used multiple times, can be added to locator/prop file and used from there
        )

        dropdown_item = self.dropdown_items
        for item in dropdown_item:
            # logging.info(f"Found: {item.text}")
            if item.text.strip() == "Pepe Pizza (Radhe Radhe)":
                logging.info("Clicking on pepe Pizza ")
                item.click()
                break


    def deal_filter(self):
        todaysdeal=self.filter
        todaysdeal.click()
        time.sleep(5)

    def category_filter(self):
        category_filter=self.browse_category
        category_filter.click()

    def cuisine_filter(self):
        cuisine_filter=self.browse_cuisine
        cuisine_filter.click()


