import pytest

from pages.cart_page import cartActions
from pages.search_page import search_Actions
from pages.signin_page import signin_Actions
from testcases.conftest import setup, testcase_logger
from utilities.readProperties import ReadConfig
from utilities.readTestData import ReadTestData


class Test_001_Signin:  # testcase id(Test_001)

    base_url = ReadConfig.getApplicationURL()

    @pytest.mark.sanity
    @pytest.mark.regression
    @testcase_logger("Test_Search_Mobile")
    def test_search_mobile(self, setup):
        self.driver = setup
        self.driver.get(Test_001_Signin.base_url)
        self.signin = signin_Actions(self.driver)
        self.signin.click_cancel()
        self.s = search_Actions(self.driver)
        self.s.clear_search_bar()
        search_param = ReadTestData.testdata()
        self.s.search(search_param["search_data1"])
        self.s.select_brand("SAMSUNG")
        self.s.sort_by("Newest First")
        self.s.select_item()
        self.cart = cartActions(self.driver)
        self.cart.add_item_to_cart()
        self.cart.clear_cart()
