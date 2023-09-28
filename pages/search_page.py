import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.customlogger import LogGenerator


class search:
    search_bar = "q"
    search_icon = "button > svg"
    brand = "//div[text()='Brand']"

    def sort_by(self, sort_category):
        return "//*[text()='" + sort_category + "']"

    def mobile_brand(self, brand):
        return "div[title='" + brand + "']"

    def select_item(self):
        return "div._3pLy-c.row"


class search_Actions:
    search_object = search()
    logger = LogGenerator.loggen()

    def __init__(self, driver):
        self.driver = driver

    def clear_search_bar(self):
        self.driver.find_element(By.NAME, search.search_bar).clear()

    def dec(self, func):
        pass

    def search(self, param):
        search_Actions.logger.info("Searching for: "+param)
        self.driver.find_element(By.NAME, search.search_bar).send_keys(param)
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, search.search_icon).click()
        time.sleep(5)
        text = self.driver.find_element(By.CSS_SELECTOR, "span._10Ermr").text
        assert param in text

    def select_brand(self, mobile_brand):
        search_Actions.logger.info("Selecting the brand as: " + mobile_brand)
        try:
            self.select_category(mobile_brand)
        except:
            self.driver.find_element(By.XPATH, search_Actions.search_object.brand).click()
            self.select_category(mobile_brand)

    def select_category(self, mobile_brand):
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, search_Actions.search_object.mobile_brand(mobile_brand)).click()

    def sort_by(self, sort_category):
        time.sleep(5)
        self.driver.find_element(By.XPATH, search_Actions.search_object.sort_by(sort_category)).click()
        search_Actions.logger.info("Sorting the item according to {} category: ".format(sort_category))

    def select_item(self):
        global wait
        wait = WebDriverWait(self.driver, timeout=60)
        global window_handles
        window_handles = self.driver.current_window_handle
        items_list = wait.until(
            expected_conditions.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, search_Actions.search_object.select_item())))
        print("List of mobile elements: ", items_list)
        for ele in items_list:
            try:
                time.sleep(5)
                ele.click()
                break
            except StaleElementReferenceException:
                pass
        wait.until(expected_conditions.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != window_handles:
                self.driver.switch_to.window(window_handle)
                break
