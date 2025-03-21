import logging
import time

from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.search.search_props import SearchProperties

class SearchPage(SearchProperties):
    def __init__(self, driver):
        self.driver = driver
        self.wait=WebDriverWait(self.driver,10)

    def search_item(self,food,excepted=None):
        searchbox = self.search_input
        searchbox.click()
        searchbox.send_keys(food)
        searchbox.send_keys(Keys.ENTER)

        self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "main-auto-suggestion"))
        )

        dropdown_item = self.dropdown_items
        if excepted:
            for item in dropdown_item:

                logging.info(f"Found: {item.text}")
                if excepted:
                    if item.text.strip() == excepted:
                        logging.info(f"{item.text.strip()} item matches with expected {excepted}")
                        item.click()
                        break


    def sort_popularity(self):
        sort_by_popularity=self.popularity_sort
        sort_by_popularity.click()
        drop=Select(sort_by_popularity)
        drop.select_by_value("lowtohigh")
        sort_by_popularity.send_keys(Keys.ESCAPE)
        time.sleep(4)


    def sort_price(self):
        sort_by_price=self.price_sort
        sort_by_price.click()
        d = Select(sort_by_price)
        d.select_by_value("3")
        sort_by_price.send_keys(Keys.ESCAPE)
        time.sleep(5)


    def todays_deal(self):
        todaysdeal=self.filter
        todaysdeal.click()
        time.sleep(5)

    def category_filter(self):
        category_filter=self.browse_category
        category_filter.click()

    def cuisine_filter(self):
        cuisine_filter=self.browse_cuisine
        cuisine_filter.click()

    def all_restaurant(self):
        select_all_restaurant=self.restaurant
        select_all_restaurant.click()

    def reset_filter(self):
        reset_filter=self.filter_reset
        reset_filter.click()




