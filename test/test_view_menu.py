import logging
import time

from page_objects.get_location.getlocation_page import GetLocationPage
from page_objects.login.login_page import LoginPage
from page_objects.search.search_page import SearchPage
from page_objects.view_menu.view_menu_page import ViewMenuPage
from setup.base_test import BaseTest


class TestViewMenu(BaseTest):

    def test_view_menu(self):
        url=self.cred["base_url"]
        self.driver.get(url)

        login=LoginPage(self.driver)
        uname=self.cred["email"]
        pwd=self.cred["password"]
        login.login_page(uname,pwd)

        location=GetLocationPage(self.driver)
        location.getlocation_page()
        time.sleep(5)

        search=SearchPage(self.driver)
        search.search_item("amore pizza","Amore Pizza (Koteshwor)")
        time.sleep(2)

        view_menu=ViewMenuPage(self.driver)
        view_menu.view_menu_page()
        logging.info("View menu page")
        time.sleep(5)





