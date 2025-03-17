from page_objects.search.search_locators import SearchLocators

class SearchProperties:

    @property
    def search_input(self):
        return self.driver.find_element(*SearchLocators.SEARCH_BOX)

    @property
    def dropdown_click(self):
        return self.driver.find_element(*SearchLocators.DROPDOWN)

    @property
    def dropdown_items(self):
        return self.driver.find_elements(*SearchLocators.DROPDOWN_ITEMS)