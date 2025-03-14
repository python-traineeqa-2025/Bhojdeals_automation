from page_objects.get_location.getlocation_properties import GetLocationProperties


class GetLocationPage(GetLocationProperties):

    def __init__(self,driver):
        self.driver=driver

    def getlocation_page(self):

        get_locationpage=self.getlocation
        get_locationpage.click()

        choose_location=self.chooselocation
        choose_location.click()

