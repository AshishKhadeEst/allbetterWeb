from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from page_objects.login import Login
from page_objects import constants
import pytest
user_name=constants.username
gmail=constants.google_email
g_password=constants.google_password

class Test_login:

    def setup(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager(version='114.0.5735.90').install()))
        self.driver.get("https://field-test.allbetterapp.com/")
        self.driver.maximize_window()

    test_data = [["ashish.kahde+1@encoresky.com", "Test@123"],
                 ["ashish.khade+1@gmail.", "Test@123"],
                 ["ashish.khade+1@encoresky.com", "test123"]]

    @pytest.mark.parametrize("username, password", test_data)
    def test_login(self,username,password):
        lg=Login(self.driver)
        lg.locate_elements(username,password)

    def test_google_login(self):
        lg=Login(self.driver)
        lg.google_login(gmail, g_password)

    def test_forgot_password(self):
        lg = Login(self.driver)
        lg.forgot_pass_word(user_name)
        # self.driver.save_screenshot('./reports/screenshots/login_page/forgot_password.png')










