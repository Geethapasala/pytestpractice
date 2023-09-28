import time

from selenium.webdriver.common.by import By

from utilities.customlogger import LogGenerator


class signin:
    cancel_button = "span._30XB9F"


class signin_Actions:
    logger = LogGenerator.loggen()
    title = "Online Shopping Site"

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def click_cancel(self):
        try:
            time.sleep(10)
            self.driver.find_element(By.CSS_SELECTOR, signin.cancel_button).click()
            signin_Actions.logger.info("clicked on cross button")
        except:
            signin_Actions.logger.info("couldn't found cross button")
        assert signin_Actions.title in self.driver.title
