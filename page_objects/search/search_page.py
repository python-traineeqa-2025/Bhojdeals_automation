import logging
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.search.search_props import SearchProperties


class SearchPage(SearchProperties):
    def __init__(self,driver):
        self.driver=driver

    def search_page(self):
        searchbox=self.search_input
        searchbox.click()
        searchbox.send_keys("pizza")
        searchbox.send_keys(Keys.ENTER)


        # dropdown=self.dropdown_click
        # li_elements = dropdown.find_elements(By.TAG_NAME, "span")
        # for li in li_elements:
        #     if li=="Amore Pizza (Koteshwor)":
        #         li.click()

        dropdown = self.dropdown_click
        li_elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.TAG_NAME, "span"))
        )
        for li in li_elements:
            print(f"Found element: {li.text}")
            if li.text == "Amore Pizza (Koteshwor)":
                print("Clicking on Amore Pizza (Koteshwor)")
                li.click()
                break



        # drp=Select(dropdown)
        # drp.select_by_visible_text("Amore Pizza (Koteshwor)")

        # logging.info(dropdown.text)






