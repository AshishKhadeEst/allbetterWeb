from page_objects.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class Sign_Up(Base):

    # def __init__(self,driver):
    #     self.driver=driver
    #     super().__init__(driver)

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
    submit=(By.XPATH,"//button[normalize-space()='Submit']")
    India=(By.XPATH,"//span[normalize-space()='India']")

    def sign_up(self,name,last_name,email,number,password,confirm_pass):
        self.EF.find_element(self.signup).click()
        time.sleep(3)
        self.EF.find_element(self.First_name).send_keys(name)
        time.sleep(3)
        self.EF.find_element(self.Last_name).send_keys(last_name)
        time.sleep(3)
        self.EF.find_element(self.Email).send_keys(email)
        actions=ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_UP).perform()
        time.sleep(3)
        self.EF.find_element(self.dropdown).click()
        time.sleep(2)
        self.EF.find_element(self.list_box)
        time.sleep(3)
        self.EF.find_element(self.search).click()
        self.EF.find_element(self.search).send_keys("Ind")
        time.sleep(3)
        self.EF.find_element(self.India).click()
        time.sleep(3)
        self.EF.find_element(self.phone).send_keys(number)
        time.sleep(3)
        actions.scroll_by_amount(10,130).perform()
        time.sleep(3)
        self.EF.find_element(self.password).send_keys(password)
        time.sleep(3)
        self.EF.find_element(self.confirm_password).send_keys(confirm_pass)
        time.sleep(2)
        self.EF.find_element(self.submit).click()
        time.sleep(3)





