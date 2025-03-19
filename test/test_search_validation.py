import logging
import time

from selenium.webdriver.common.by import By

from page_objects.get_location.getlocation_page import GetLocationPage
from page_objects.search.search_page import SearchPage
from setup.base_test import BaseTest


class TestSearchValidation(BaseTest):
    def test_search_validation(self):
        url = self.cred["base_url"]
        self.driver.get(url)

        getlocation = GetLocationPage(self.driver)
        getlocation.getlocation_page()

        search = SearchPage(self.driver)
        search.invalid_search()
        time.sleep(5)

        #inf=self.driver.find_element(By.XPATH,"//div[@class='restaurant-type']//h2")
        #self.assertTrue(inf.is_displayed(),"Pizza Hut(Thimi)")

    def test_filter(self):
        url = self.cred["base_url"]
        self.driver.get(url)

        getlocation = GetLocationPage(self.driver)
        getlocation.getlocation_page()
        logging.info("Got location")
        search = SearchPage(self.driver)
        search.deal_filter()


    def test_category_filter(self):
        url = self.cred["base_url"]
        self.driver.get(url)

        getlocation = GetLocationPage(self.driver)
        getlocation.getlocation_page()
        logging.info("Got location")
        search = SearchPage(self.driver)
        self.driver.execute_script('scrollBy(0,1000)')
        search.category_filter()
        time.sleep(5)

    def test_cuisine_filter(self):
        url = self.cred["base_url"]
        self.driver.get(url)

        getlocation = GetLocationPage(self.driver)
        getlocation.getlocation_page()
        logging.info("Got location")

        search = SearchPage(self.driver)
        self.driver.execute_script('scrollBy(0,1000)')
        search.cuisine_filter()
        time.sleep(5)







