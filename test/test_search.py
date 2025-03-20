import time
from page_objects.get_location.getlocation_page  import GetLocationPage
from page_objects.login.login_page import LoginPage
from page_objects.search.search_page import SearchPage
from setup.base_test import BaseTest
class TestSearch (BaseTest):
    def test_search(self):
        url = self.cred["base_url"]
        self.driver.get(url)

        login = LoginPage(self.driver)
        uname = self.cred["email"]
        pwd = self.cred["password"]
        login.login_page(uname,pwd)

        getlocation = GetLocationPage(self.driver)
        getlocation.getlocation_page()

        search = SearchPage(self.driver)
        search.search_item("amore pizza","Amore Pizza (Koteshwor)")
        time.sleep(6)


