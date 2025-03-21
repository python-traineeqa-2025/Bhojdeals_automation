import logging
from page_objects.add_tocart.add_tocart_props import AddToCartProperties


class AddToCartPage(AddToCartProperties):

    def __init__(self,driver):
        self.driver=driver

    def add_tocart_page(self):
        add_to_cart=self.add_button
        add_to_cart.click()

        add_item=self.add_item
        add_item.click()
        item_name=self.item_name
        logging.info(f"Item added to cart:{item_name.text}")
        item_price=self.item_price
        logging.info(f"Item price:{item_price.text}")





