import time
from selenium.webdriver.common.by import By

from utilities.customlogger import LogGenerator
from utilities.reusablecomponents import scroll_to_end


class cart:
    add_to_cart = "//button[@class='_2KpZ6l _2U9uOA _3v1-ww']"
    remove_button = "//div[contains(text(),'Remove')]"
    remove_button_alert = "div._3dsJAO._24d-qY.FhkMJZ"
    empty_cart = "div._1LCJ1U"


class cartActions:
    logger = LogGenerator.loggen()

    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self):
        cartActions.logger.info("Adding item to cart")
        self.driver.find_element(By.XPATH, cart.add_to_cart).click()

    def clear_cart(self):
        time.sleep(5)
        scroll_to_end(self.driver)
        time.sleep(5)
        cartActions.logger.info("Removing item from cart")
        self.driver.find_element(By.XPATH, cart.remove_button).click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, cart.remove_button_alert).click()
        time.sleep(5)
        assert self.driver.find_element(By.CSS_SELECTOR, cart.empty_cart) is not None
