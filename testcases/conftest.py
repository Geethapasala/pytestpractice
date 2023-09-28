import functools

import pytest
from selenium import webdriver

from utilities.customlogger import LogGenerator
from utilities.readProperties import ReadConfig

logger = LogGenerator.loggen()

browsers = ReadConfig.get_browsers()


@pytest.fixture(scope="function", params=[browsers[0], browsers[1]])
def setup(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        logger.info("Launching the CHROME Browser")
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        logger.info("Launching the FIREFOX Browser")
    elif request.param == "edge":
        driver = webdriver.Edge()
        logger.info("Launching the EDGE Browser")
    else:
        driver = webdriver.Chrome()
        logger.info("Launching the CHROME Browser")
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        screenshot_name = f".\\screenshots\\{item.name}.png"
        driver = item.funcargs.get("setup")
        if driver:
            driver.execute_script("return document.body.scrollHeight")
            driver.save_screenshot(screenshot_name)
            logger.info(f"Screenshot saved as {screenshot_name}")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# # HTML REPORT
# def pytest_configure(config):
#     config.metadata['Project Name'] = "flipkartTests"
#     config.metadata['Module Name'] = "Login"
#     config.metadata['Tester'] = "Geethanjali"
#     config.metadata['NAme'] = "Geetha"
#
#

# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)


def testcase_logger(testcase_name):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"Testcase '{testcase_name}' has started.")
            func(*args, **kwargs)
            logger.info(f"Testcase '{testcase_name}' has ended.")

        return wrapper

    return decorator
