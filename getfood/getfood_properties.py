from getfood.getfood_locators import GetFoodLocators


class GetFoodProperties(GetFoodLocators):

    @property
    def getfood(self):
        return self.driver.find_element(*GetFoodLocators.GETFOOD)

    @property
    def getlocation(self):
        return self.driver.find_element(*GetFoodLocators.LOCATION_BHAKTAPUR)

