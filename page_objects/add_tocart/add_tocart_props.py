from page_objects.add_tocart.add_tocart_locators import AddToCartLocators


class AddToCartProperties(AddToCartLocators):

    @property
    def add_button(self):
        return self.driver.find_element(*AddToCartLocators.ADD_BUTTON)

    @property
    def add_item(self):
        return self.driver.find_element(*AddToCartLocators.ADD_ITEM)

    @property
    def item_name(self):
        return self.driver.find_element(*AddToCartLocators.ITEM_NAME)

    @property
    def item_price(self):
        return self.driver.find_element(*AddToCartLocators.ITEM_PRICE)