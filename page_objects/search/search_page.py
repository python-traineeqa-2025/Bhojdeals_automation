import logging

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.search.search_props import SearchProperties

class SearchPage(SearchProperties):
    def __init__(self, driver):
        self.driver = driver

    def search_page(self):
        searchbox = self.search_input
        searchbox.click()
        searchbox.send_keys("pizza")
        searchbox.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "main-auto-suggestion"))
        )

        dropdown_item = self.dropdown_items

        for item in dropdown_item:
            logging.info(f"Found: {item.text}")
            if item.text.strip() == "Amore Pizza(Koteshwor)":
                logging.info("Clicking on Amore Pizza (Koteshwor)")
                item.click()
                break
