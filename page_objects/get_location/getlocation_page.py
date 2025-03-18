from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.get_location.getlocation_properties import GetLocationProperties

from selenium.webdriver.support import expected_conditions as EC
class GetLocationPage(GetLocationProperties):

    def __init__(self,driver):
        self.driver=driver

    def getlocation_page(self):
        get_locationpage=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,"//h2[normalize-space()='Get Food & Grocery delivered']")))
        get_locationpage.click()

        choose_location=self.chooselocation
        choose_location.click()

