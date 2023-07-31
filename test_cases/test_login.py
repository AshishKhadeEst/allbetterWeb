import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from page_objects.login import Login
from page_objects import constants

username=constants.username
password=constants.password
invalid_username=constants.invalid_username
invalid_password=constants.invalid_password
gmail=constants.google_email
g_password=constants.google_password

class Test_Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='114.0.5735.90').install()))
        self.driver.get("https://field-test.allbetterapp.com/")
        self.driver.maximize_window()

    def test_with_valid_credentials(self):
        lg=Login(self.driver)
        lg.input_username(username)
        time.sleep(2)
        lg.input_password(password)
        lg.submit_button()
        self.driver.save_screenshot('./reports/screenshots/login_page/valid.credentials.png')

    def test_with_invalid_email(self):
        lg=Login(self.driver)
        lg.input_username(invalid_username)
        lg.input_password(password)
        lg.submit_button()
        self.driver.save_screenshot('./reports/screenshots/login_page/invalid_email.png')

    def test_with_invalid_password(self):
        lg = Login(self.driver)
        lg.input_username(username)
        lg.input_password(invalid_password)
        lg.submit_button()

    def test_google_login(self):
        lg=Login(self.driver)
        lg.google_login(gmail,g_password)

    def test_forgot_password(self):
        lg = Login(self.driver)
        lg.forgot_pass_word(username)
        self.driver.save_screenshot('./reports/screenshots/login_page/forgot_password.png')

    def tearDown(self) -> None:
        self.driver.quit()









