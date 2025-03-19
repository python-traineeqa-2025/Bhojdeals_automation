
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
        self.driver = driver

    def search_page(self):
        searchbox = self.search_input
        searchbox.click()
        searchbox.send_keys("amore pizza")
        searchbox.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "main-auto-suggestion"))
        )

        dropdown_item = self.dropdown_items

        for item in dropdown_item:
            # logging.info(f"Found: {item.text}")
            if item.text.strip() == "Amore Pizza (Koteshwor)":
                logging.info("Clicking on Amore Pizza (Koteshwor)")
                item.click()
                break

    def invalid_search(self):
        searchbox = self.search_input
        searchbox.click()
        searchbox.send_keys("pizz")
        searchbox.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME,"main-auto-suggestion"))
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




