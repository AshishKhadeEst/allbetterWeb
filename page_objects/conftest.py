import pytest
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from page_objects import constants
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

#Edge
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

username=constants.username
password=constants.password

@pytest.fixture(scope="class")
def setup(request):
    browser = "chrome"
    if browser.lower() == "chrome":

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    else:
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    driver.get("https://field-test.allbetterapp.com/")
    time.sleep(3)
    driver.maximize_window()
    time.sleep(4)
    driver.find_element(By.NAME, "email").send_keys(username)
    time.sleep(1)
    driver.find_element(By.NAME, "password").send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH,"//button[normalize-space()='Log In']").click()
    time.sleep(1)
    request.cls.driver = driver
    pytest.driver=driver
    yield driver


