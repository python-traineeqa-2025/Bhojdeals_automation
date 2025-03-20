import logging
import time
from page_objects.add_tocart.add_tocart_page import AddToCartPage
from page_objects.checkout.checkout_page import CheckoutPage
from page_objects.get_location.getlocation_page import GetLocationPage
from page_objects.login.login_page import LoginPage
from page_objects.search.search_page import SearchPage
from page_objects.view_menu.view_menu_page import ViewMenuPage
from setup.base_test import BaseTest
from selenium.webdriver.support import expected_conditions as EC

class TestCheckout(BaseTest):
    def test_checkout(self):

        url = self.cred["base_url"]
        self.driver.get(url)
        logging.info("driver initialized")
        time.sleep(5)

        login = LoginPage(self.driver)
        uname = self.cred["email"]
        pwd = self.cred["password"]
        login.login_page(uname, pwd)
        logging.info("Successful Login")

        location = GetLocationPage(self.driver)
        location.getlocation_page()
        time.sleep(5)
        logging.info("got location")

        search=SearchPage(self.driver)
        search.search_page("amore pizza","Amore Pizza (Koteshwor)")
        time.sleep(2)
        logging.info("search product")

        view_menu = ViewMenuPage(self.driver)
        view_menu.view_menu_page()
        logging.info("View menu page")
        time.sleep(5)

        add_cart = AddToCartPage(self.driver)
        add_cart.add_tocart_page()
        time.sleep(5)

        checkout=CheckoutPage(self.driver)

        checkout.checkout_page("New Baneshwor","Add extra chilli flakes")

        time.sleep(4)

