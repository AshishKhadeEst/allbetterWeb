from page_objects.base import Base
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from utility.elementary_function import Elem_Func

class Login(Base):

    log= Elem_Func.custom_logger()
    Email=(By.NAME,"email")
    Password=(By.NAME,"password")
    Submit=(By.XPATH,"//button[normalize-space()='Log In']")
    forgot_password=(By.XPATH,"//a[contains(text(),'Forgot password?')]")
    send_email=(By.XPATH,"//button[normalize-space()='Send Email']")
    google_signin=(By.XPATH,"//button[@type='button']")
    another_account=(By.XPATH,"//div[@class='BHzsHc']")
    google_email=(By.ID,"identifierId")
    next_button=(By.ID,"identifierNext")
    google_password=(By.XPATH,"//input[@name='password']")
    checkbox=(By.XPATH,"//input[@type='checkbox']")
    next=(By.XPATH,"//span[normalize-space()='Next']")
    wrong_user=(By.CLASS_NAME,"notification-description")
    wrong_password=(By.CLASS_NAME,"notification-description")

    def locate_elements(self,username,password):
        self.EF.find_element(self.Email).send_keys(username)
        self.EF.find_element(self.Password).send_keys(password)
        self.EF.find_element(self.Submit).click()

    def google_login(self,email,password):
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(10,200).perform()
        time.sleep(2)
        self.EF.find_element(self.google_signin).click()
        time.sleep(3)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle!=parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.EF.find_element(self.google_email).send_keys(email)
        self.EF.find_element(self.next_button).click()
        # self.driver.save_screenshot('./reports/screenshots/login_page/google_login.png')
        self.EF.find_element(self.google_password).send_keys(password)
        self.EF.find_element(self.checkbox).click()
        self.EF.find_element(self.next).click()

    def forgot_pass_word(self,username):

        self.EF.find_element(self.forgot_password).click()
        time.sleep(3)
        self.EF.find_element(self.Email).send_keys(username)
        self.EF.find_element(self.send_email).click()
        self.log.info("Forgot Password success")

    def msg_for_wrong_user(self):
        return self.EF.find_element(self.wrong_user).text

    def msg_for_wrong_password(self):
        self.log.info("Message for wrong Password")
        return self.EF.find_element(self.wrong_password).text













