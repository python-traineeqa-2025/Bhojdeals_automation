import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from page_objects.checkout.checkout_props import CheckoutProperties


class CheckoutPage(CheckoutProperties):

    def __init__(self,driver):
        self.driver=driver

    def checkout_page(self,address):
        #checkout button click
        checkout_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Proceed to check out']")))
        checkout_button.click()
        time.sleep(5)

        #click on add delivery button
        add_delivery_btn= WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='addnew-btn']")))
        add_delivery_btn.click()

        #enter address in search box
        add_address=self.add_deliver_address
        add_address.click()
        add_address.send_keys(address)
        # add_address.send_keys(Keys.ENTER)
        time.sleep(5)

        #close the address popup
        close=self.close_address
        close.click()
        time.sleep(5)

        #choose option for call for confirmation
        call_confirmation=self.confirm_call
        call_confirmation.click()
        time.sleep(6)

        #delivery day
        delivery_day = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//div[@class='view']//li[2]")))
        delivery_day.click()
        time.sleep(6)















