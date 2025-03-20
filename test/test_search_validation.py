import logging
import time
from page_objects.get_location.getlocation_page import GetLocationPage
from page_objects.search.search_page import SearchPage
from setup.base_test import BaseTest

class TestSearchValidation(BaseTest):
    def test_autocorrect_sorting(self):
        url = self.cred["base_url"]
        self.driver.get(url)
                                        
        getlocation = GetLocationPage(self.driver)
        getlocation.getlocation_page()

        search = SearchPage(self.driver)
        search.search_item("piz","Pizza")
        time.sleep(10)
        logging.info("auto correct search completed")

        # sort by popularity
        search.sort_popularity()
        time.sleep(10)
        logging.info("sorted by popularity")

        # sort by price
        search.sort_price()
        time.sleep(10)
        logging.info("sorted by price")


    def test_filter(self):
        url = self.cred["base_url"]
        self.driver.get(url)
        #get location
        getlocation = GetLocationPage(self.driver)
        getlocation.getlocation_page()
        logging.info("Got location")
        time.sleep(10)
        #search
        search = SearchPage(self.driver)
        #deal filter
        search.deal_filter()
        time.sleep(10)
        logging.info("sorted by filter")


        #cuisine filter
        self.driver.execute_script('scrollBy(0,1000)')
        search.cuisine_filter()
        time.sleep(10)

        # self.driver.refresh()
        # getlocation.getlocation_page()



        # category filter
        search.category_filter()
        time.sleep(10)
        logging.info("sorted by category")












