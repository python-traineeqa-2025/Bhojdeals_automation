from getfood.getfood_properties import GetFoodProperties


class GetFoodPage(GetFoodProperties):

    def __init__(self,driver):
        self.driver=driver

    def getfood_page(self):

        choose_getfood=self.getfood
        choose_getfood.click()

        choose_location=self.getlocation
        choose_location.click()

