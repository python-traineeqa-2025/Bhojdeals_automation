import logging
from page_objects.add_tocart.add_tocart_props import AddToCartProperties


class AddToCartPage(AddToCartProperties):

    def __init__(self,driver):
        self.driver=driver

    def add_tocart_page(self):
        add_to_cart=self.add_button
        add_to_cart.click()

        quantity_add=self.add_quantity
        quantity_add.click()
        item_name=self.item_name
        logging.info(f"Item added to cart:{item_name.text}")
        item_price=self.item_price
        logging.info(f"Item price:{item_price.text}")





