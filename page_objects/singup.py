from page_objects.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class Sign_Up(Base):

    signup=(By.LINK_TEXT,"Sign up")
    First_name=(By.XPATH,"//input[@placeholder='First name']")
    Last_name=(By.XPATH,"//input[@placeholder='Last name']")
    Email=(By.XPATH,"//input[@placeholder='Email']")
    list_box=(By.XPATH,"//ul[@role='listbox']")
    country_highlight=(By.XPATH,"//span[normalize-space()='+91']")
    dropdown=(By.XPATH,"//div[@class='flag-dropdown ']")
    search=(By.XPATH,"//input[@placeholder='search']")
    phone=(By.NAME,"phone_number")
    password=(By.XPATH,"//input[@placeholder='Password']")
    confirm_password=(By.XPATH,"//input[@placeholder='Confirm Password']")
    referral_code=(By.XPATH,"//input[@placeholder='Referral Code (optional)']")
    submit=(By.XPATH,"//button[normalize-space()='Sign up']")
    India=(By.XPATH,"//span[normalize-space()='India']")
    google_button=(By.XPATH,"//button[@type='button']")
    g_email=(By.XPATH,"//input[@id='identifierId']")
    g_password=(By.XPATH,"//input[@name='password']")
    next_button=(By.XPATH,"//span[normalize-space()='Next']")

    def sign_up(self,name,last_name,email,number,password,confirm_pass):
        self.EF.find_element(self.signup).click()
        self.EF.find_element(self.First_name).send_keys(name)
        self.EF.find_element(self.Last_name).send_keys(last_name)
        self.EF.find_element(self.Email).send_keys(email)
        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_UP).perform()
        self.EF.find_element(self.dropdown).click()
        self.EF.find_element(self.list_box)
        self.EF.find_element(self.search).click()
        self.EF.find_element(self.search).send_keys("Ind")
        self.EF.find_element(self.India).click()
        self.EF.find_element(self.phone).send_keys(number)
        actions.scroll_by_amount(10,130).perform()
        self.EF.find_element(self.password).send_keys(password)
        self.EF.find_element(self.confirm_password).send_keys(confirm_pass)
        self.EF.find_element(self.submit).click()

    def google_signup(self,gmail,password):
        self.EF.find_element(self.signup).click()
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 200).perform()
        time.sleep(2)
        self.EF.find_element(self.google_button).click()
        time.sleep(3)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.EF.find_element(self.g_email).send_keys(gmail)
        self.EF.find_element(self.next_button).click()
        self.EF.find_element(self.g_password).send_keys(password)
        self.EF.find_element(self.next_button).click()






