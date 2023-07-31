from page_objects.base import Base
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

class Login(Base):

    # def __init__(self,driver):
    #     self.driver=driver
    #     super().__init__(driver)

    Email=(By.NAME,"email")
    Password=(By.NAME,"password")
    Submit=(By.XPATH,"//button[normalize-space()='Submit']")
    forgot_password=(By.XPATH,"//a[normalize-space()='Forgot Password?']")
    send_email=(By.XPATH,"//button[normalize-space()='Send Email']")
    google_signin=(By.XPATH,"//span[@class='flex items-center justify-center']")
    another_account=(By.XPATH,"//div[@class='BHzsHc']")
    google_email=(By.ID,"identifierId")
    next_button=(By.ID,"identifierNext")
    google_password=(By.XPATH,"//input[@name='password']")
    checkbox=(By.XPATH,"//input[@type='checkbox']")
    next=(By.XPATH,"//span[normalize-space()='Next']")

    def input_username(self,username):
        self.EF.find_element(self.Email).send_keys(username)
        time.sleep(3)

    def input_password(self,password):
        self.EF.find_element(self.Password).send_keys(password)
        time.sleep(3)

    def google_login(self,email,password):
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(10,100).perform()
        time.sleep(3)
        self.EF.find_element(self.google_signin).click()
        time.sleep(3)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        time.sleep(3)
        all_handles = self.driver.window_handles
        print(all_handles)
        time.sleep(3)
        for handle in all_handles:
            if handle!=parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.EF.find_element(self.google_email).send_keys(email)
        time.sleep(3)
        self.EF.find_element(self.next_button).click()
        time.sleep(3)
        self.driver.save_screenshot('./reports/screenshots/login_page/google_login.png')
        time.sleep(3)
        self.EF.find_element(self.google_password).send_keys(password)
        time.sleep(3)
        self.EF.find_element(self.checkbox).click()
        time.sleep(3)
        self.EF.find_element(self.next).click()
        time.sleep(3)

    def submit_button(self):
        self.EF.find_element(self.Submit).click()
        time.sleep(3)

    def forgot_pass_word(self,username):
        self.EF.find_element(self.forgot_password).click()
        time.sleep(3)
        self.EF.find_element(self.Email).send_keys(username)
        time.sleep(3)
        self.EF.find_element(self.send_email).click()
        time.sleep(3)








