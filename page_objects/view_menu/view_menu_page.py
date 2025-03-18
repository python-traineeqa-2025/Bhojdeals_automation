from selenium import webdriver
from unicodedata import category

from page_objects.view_menu.view_menu_props import ViewMenuPropertries


class ViewMenuPage(ViewMenuPropertries):

    def __init__(self, driver):
        self.driver = driver


    def view_menu_page(self):
        view=self.select_restaurant
        view.click()

        view_category=self.select_category
        view_category.click()

        # view_map=self.view_map
        # view_map.click()






