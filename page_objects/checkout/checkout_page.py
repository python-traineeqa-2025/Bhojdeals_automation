import logging
import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from page_objects.checkout.checkout_props import CheckoutProperties


class CheckoutPage(CheckoutProperties):

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver, 10)

    def checkout_page(self,address,note):

        #checkout button click
        checkout_button = self.wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Proceed to check out']")))
        checkout_button.click()
        time.sleep(5)
        logging.info("checkout button clicked")

        #click on add delivery button
        # self.driver.execute_script('scrollBy(0,1000)')
        add_delivery_btn= self.wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='addnew-btn']")))
        add_delivery_btn.click()
        logging.info("add delivery address button clicked ")

        add_address = self.add_delivery_address
        add_address.click()
        add_address.send_keys(address)
        # add_address.send_keys(Keys.ENTER)
        logging.info("address added")
        time.sleep(5)
        # search_box = driver.find_element(By.XPATH, "//input[@type='text']")
        # search_box.send_keys("New")
        # WebDriverWait(self.driver, 5).until(
        #     EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'pac-item')]"))
        # )

        # WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//li")))
        # # Use keyboard navigation to select the desired address
        # actions = ActionChains(self.driver)
        # actions.send_keys(Keys.DOWN).perform()  # Press Down Arrow
        # actions.send_keys(Keys.DOWN).perform()  # Press Down Arrow again (repeat as needed)
        # actions.send_keys(Keys.ENTER).perform()  # Press Enter to select the address
        #
        # # Wait a bit to ensure the selection is applied
        # WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element_value(SEARCH_BOX, "New Baneshwor"))
        #
        # print("Address selected successfully!")

        # Get all suggestions
        # suggestions = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'pac-item')]")
        #
        # # Loop through the options and click the desired one
        # for suggestion in suggestions:
        #     logging.info(suggestion.text)  # Print all suggestions
        #     if "New Baneshwor, Kathmandu, Nepal" in suggestion.text:  # Choose the specific address
        #         suggestion.click()
        #         break








        #close the address popup
        close=self.close_address
        close.click()
        time.sleep(5)

        #choose option for call for confirmation
        call_confirmation=self.wait.until(EC.visibility_of_element_located(self.CONFIRMATION_CALL))
        call_confirmation.click()
        logging.info("Call for confirmation checked")
        time.sleep(6)

        #delivery day
        delivery_day =self.wait.until(
        EC.element_to_be_clickable((By.XPATH,"//div[@class='view']//li[2]")))
        delivery_day.click()
        time.sleep(6)
        logging.info("delivery day set to tomorrow")
        #
        extra_note=self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Driver Note')]/textarea")))
        extra_note.click()
        extra_note.send_keys(note)
        # logging.info("Extra note added to the driver")
        #
        payment=self.payment_method
        payment.click()
        logging.info("checked on the payment method")



















