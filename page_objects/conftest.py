import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

#Edge
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#Chrome
# options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications": 2}
# options.add_experimental_option("prefs", prefs)

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))

#Firefox
# options = webdriver.FirefoxOptions()
# options.set_preference('dom.webnotifications.enabled', False)

#Edge
# options = webdriver.EdgeOptions()
# Prefs=("profile.default_content_setting_values.notifications", 2)
# options.set_capability("prefs",Prefs)

# import Login_details
# username=Login_details.USERNAME
# password=Login_details.PASSWORD

@pytest.fixture(scope="function")
def setup(request):
    browser = "chrome"
    if browser.lower() == "chrome":

        driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='114.0.5735.90').install()))

    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    else:
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    driver.get("https://field-test.allbetterapp.com/")
    time.sleep(3)
    driver.maximize_window()
    time.sleep(4)
    # driver.find_element(By.NAME, "username").send_keys(username)
    # time.sleep(1)
    # driver.find_element(By.NAME, "password").send_keys(password)
    # time.sleep(1)
    # driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    # time.sleep(1)
    request.cls.driver = driver

