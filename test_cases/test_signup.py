import pytest
from page_objects.conftest import setup
from page_objects.singup import Sign_Up
from page_objects import constants
import allure

name=constants.name
last_name=constants.lastname
email=constants.email
phone=constants.phone
password=constants.pass_word
confirm_password=constants.confirm_password
invalid_email=constants.invalid_email
invalid_phone=constants.invalid_phone
wrong_password=constants.wrong_password
gmail=constants.g_mail
g_pass=constants.g_password

@pytest.mark.usefixtures("setup")
class Test_Signup:

    def test_sign_up_successful(self):
        object=Sign_Up(self.driver)
        object.sign_up(name,last_name,email,phone,password,confirm_password)
        self.driver.save_screenshot('./reports/screenshots/signup_page/sign_up_success.png')

    def test_sign_up_invalid_email(self):
        object = Sign_Up(self.driver)
        object.sign_up(name,last_name,invalid_email,phone,password,confirm_password)
        self.driver.save_screenshot('./reports/screenshots/signup_page/sign_up_invalid_email.png')

    def test_sign_up_invalid_phone(self):
        object = Sign_Up(self.driver)
        object.sign_up(name,last_name,email,invalid_phone,password,confirm_password)
        self.driver.save_screenshot('./reports/screenshots/signup_page/sign_up_invalid_phone.png')

    def test_password_do_not_match(self):
        object = Sign_Up(self.driver)
        object.sign_up(name,last_name,email,phone,password,wrong_password)
        self.driver.save_screenshot('./reports/screenshots/signup_page/password_do_not_match.png')

    def test_google_signup(self):
        object = Sign_Up(self.driver)
        object.google_signup(gmail,g_pass)




