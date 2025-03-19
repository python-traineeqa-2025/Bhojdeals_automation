import json
import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    logger = logging.getLogger(__name__)

    @pytest.fixture(autouse=True, scope="class")
    def setup_method(self,request):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=chrome_options)
        # driver=webdriver.Chrome()
        self.driver=driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        cred_path=r"C:\Users\anushagi\OneDrive - Infinite Computer Solutions (India) Limited\Documents\Bhojdeals_automation\creds\cred.json"
        with open(cred_path,"r") as file:
            self.cred=json.load(file)

        request.cls.driver=self.driver
        request.cls.cred=self.cred




        yield
        self.driver.quit()