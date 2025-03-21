import logging
import time

from page_objects.add_tocart.add_tocart_page import AddToCartPage
from page_objects.get_location.getlocation_page import GetLocationPage
from page_objects.login.login_page import LoginPage
from page_objects.search.search_page import SearchPage
from page_objects.view_menu.view_menu_page import ViewMenuPage
from setup.base_test import BaseTest


class TestAddToCart(BaseTest):
    def test_add_to_cart(self):
        url = self.cred["base_url"]
        self.driver.get(url)
        logging.info("driver initialized")

        loginpage = LoginPage(self.driver)
        email = self.cred["email"]
        pwd = self.cred["password"]
        loginpage.login_page(email,pwd)
        logging.info("Login successful")
        time.sleep(3)

        getlocation_p=GetLocationPage(self.driver)
        getlocation_p.getlocation_page()
        time.sleep(3)

        search = SearchPage(self.driver)
        search.search_item("amore pizza","Amore Pizza (Koteshwor)")
        time.sleep(3)

        view_menu = ViewMenuPage(self.driver)
        view_menu.view_menu_page()
        time.sleep(5)

        add_cart=AddToCartPage(self.driver)
        add_cart.add_tocart_page()
        time.sleep(3)











