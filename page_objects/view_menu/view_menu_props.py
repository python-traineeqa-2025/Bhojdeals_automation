from page_objects.view_menu.view_menu_locators import ViewMenuLocators


class ViewMenuPropertries(ViewMenuLocators):

    @property
    def select_restaurant(self):
        return self.driver.find_element(*ViewMenuLocators.RESTAURANT)

    @property
    def select_category(self):
        return self.driver.find_element(*ViewMenuLocators.MENU_CATEGORY)