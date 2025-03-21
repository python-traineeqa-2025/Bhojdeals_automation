import logging

from selenium.webdriver.common.by import By

from page_objects.add_tocart.add_tocart_props import AddToCartProperties


class AddToCartPage(AddToCartProperties):

    def __init__(self,driver):
        self.driver=driver

    def add_tocart_page(self):
        add_to_cart=self.add_button
        add_to_cart.click()

        add_item=self.add_item
        add_item.click()
        item_name=self.driver.find_element(By.XPATH,"//h4[normalize-space(text())='Chicken C Mo:Mo']")
        logging.info(f"Item added succesfully to cart:{item_name.text}")





