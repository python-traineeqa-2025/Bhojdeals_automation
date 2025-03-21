from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.get_location.getlocation_properties import GetLocationProperties

from selenium.webdriver.support import expected_conditions as EC
class GetLocationPage(GetLocationProperties):

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    def getlocation_page(self):
        get_locationpage=self.wait.until(EC.presence_of_element_located(self.GETLOCATION))
        get_locationpage.click()

        choose_location=self.chooselocation
        choose_location.click()

