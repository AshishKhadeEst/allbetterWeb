import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from page_objects.base import Base
import pyautogui


class Add_Employees(Base):

    add_employees=(By.XPATH,"//span[@class='flex items-center justify-center']")
    upload_image=(By.XPATH,"//div[contains(@class,'upload cursor-pointer')]")
    first_name=(By.XPATH,"//input[@placeholder='First name']")
    last_name=(By.XPATH,"//input[@placeholder='Last name']")
    search_address=(By.XPATH,"//input[@placeholder='Search Places ...']")
    auto_suggest=(By.XPATH,"//span[normalize-space()='Vijay Nagar, Indore, Madhya Pradesh, India']")
    auto_adddress_2=(By.XPATH,"//span[normalize-space()='Nanda Nagar, Indore, Madhya Pradesh, India']")
    address=(By.XPATH,"//input[@placeholder='Address']")
    employee_notes=(By.XPATH,"//textarea[@placeholder='Employee notes']")
    select_category=(By.XPATH,"//label[normalize-space()='Select category']")
    categories_item=(By.XPATH,"//body/div[contains(@class,'drawer-portal')]/div[contains(@class,'drawer-overlay drawer-overlay-after-open')]/div[contains(@role,'dialog')]/div[contains(@class,'drawer-content vertical')]/div[contains(@class,'drawer-body')]/div/div/div/div/div")
    done=(By.XPATH,"//button[normalize-space()='Done']")
    flag_dropdown=(By.XPATH,"//div[@class='flag-dropdown ']")
    list_box=(By.XPATH,"//ul[@role='listbox']")
    carpet_cleaning=(By.XPATH,"//span[contains(text(),'Carpet Cleaning')]")
    search_box=(By.XPATH,"//input[@placeholder='search']")
    country=(By.XPATH,"//span[normalize-space()='India']")
    phone_number=(By.XPATH,"//input[@placeholder='1 (702) 123-4567']")
    email=(By.XPATH,"//input[@placeholder='Email']")
    password=(By.XPATH,"//input[@placeholder='Password']")
    confirm_password=(By.XPATH,"//input[@placeholder='Confirm password']")
    send_otp=(By.XPATH,"//span[contains(text(),'Send OTP')]")
    otp_group=(By.XPATH,"//div[contains(@class,'otp-group')]")
    edit_button=(By.XPATH,"//tbody/tr[2]/td[6]/div[1]/div[1]")
    save_button=(By.XPATH,"//span[contains(text(),'Save')]")
    switch_toggle=(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[9]/td[5]/div[1]/div[1]/label[1]/div[1]")

    def add_employee(self,name,lastname,phone,email,pass_word,confirm_p):
        self.click_on_settings()
        self.click_on_employees()
        self.EF.find_element(self.add_employees).click()
        file_input = self.EF.find_element(self.upload_image)
        file_input.click()
        time.sleep(3)
        image_path=r'C:\Users\Quick\Desktop\profile_image.jpg'
        pyautogui.write(image_path)
        pyautogui.press('enter')
        time.sleep(3)
        self.EF.find_element(self.first_name).send_keys(name)
        self.EF.find_element(self.last_name).send_keys(lastname)
        self.EF.find_element(self.flag_dropdown).click()
        self.EF.find_element(self.list_box)
        self.EF.find_element(self.search_box).send_keys("Ind")
        self.EF.find_element(self.country).click()
        self.EF.find_element(self.phone_number).send_keys(phone)
        self.EF.find_element(self.email).send_keys(email)
        self.EF.find_element(self.password).send_keys(pass_word)
        self.EF.find_element(self.confirm_password).send_keys(confirm_p)
        self.EF.find_element(self.search_address).send_keys("Vijay nagar Indore")
        self.EF.find_element(self.auto_suggest).click()
        self.EF.find_element(self.employee_notes).send_keys("No notes now")
        self.EF.find_element(self.select_category).click()
        categories=self.EF.find_elements(self.categories_item)
        for category in categories:
            category.click()
        self.EF.find_element(self.done).click()
        self.EF.find_element(self.send_otp).click()
        self.driver.close()

    def edit_employee(self,name,lastname,email):
        self.click_on_settings()
        self.click_on_employees()
        self.EF.find_element(self.edit_button).click()
        file_input = self.EF.find_element(self.upload_image)
        file_input.click()
        time.sleep(3)
        image_path = r'C:\Users\Quick\Desktop\profile_image.jpg'
        pyautogui.write(image_path)
        pyautogui.press('enter')
        time.sleep(3)
        edit_name=self.EF.find_element(self.first_name)
        edit_name.send_keys(Keys.BACKSPACE*50)
        edit_name.send_keys(name)
        edit_last_name=self.EF.find_element(self.last_name)
        edit_last_name.send_keys(Keys.BACKSPACE*50)
        edit_last_name.send_keys(lastname)
        # edit_email=self.EF.find_element(self.email)
        # edit_email.send_keys(Keys.BACKSPACE*100)
        # edit_email.send_keys(email)
        self.EF.find_element(self.search_address).send_keys("Nanda nagar Indore")
        self.EF.find_element(self.auto_adddress_2).click()
        self.EF.find_element(self.employee_notes).send_keys("New notes")
        self.EF.find_element(self.select_category).click()
        self.EF.find_element(self.carpet_cleaning).click()
        self.EF.find_element(self.done).click()
        self.EF.find_element(self.save_button).click()
        self.driver.close()

    def change_status(self):
        self.click_on_settings()
        self.click_on_employees()
        self.EF.find_element(self.switch_toggle).click()
        self.driver.close()

















