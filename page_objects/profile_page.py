import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from page_objects.base import Base
import pyautogui


class Edit_Profile(Base):

    company_profile=(By.XPATH,"//div[@class='upload cursor-pointer']")
    company_name=(By.XPATH,"//input[@placeholder='Company name']")
    email=(By.XPATH,"//input[@placeholder='Email']")
    flag_dropdown=(By.XPATH,"//div[@class='flag-dropdown ']")
    search=(By.XPATH,"//input[@placeholder='search']")
    list_box=(By.XPATH,"//ul[@role='listbox']")
    country_name=(By.XPATH,"//span[normalize-space()='India']")
    phone=(By.XPATH,"//input[@placeholder='1 (702) 123-4567']")
    role=(By.XPATH,"//input[@placeholder='Role in company']")
    business_license_number=(By.XPATH,"//input[@placeholder='Business license number']")
    insurance_number=(By.XPATH,"//input[@placeholder='Insurance number']")
    company_size=(By.XPATH,"//input[@value='1']")
    business_years=(By.XPATH,"//input[@value='1-2']")
    specialization=(By.XPATH,"//div[@class='form-item vertical']//div//div[@class='card-body card-gutterless']")
    categories=(By.XPATH,"//body/div[contains(@class,'drawer-portal')]/div[contains(@class,'drawer-overlay drawer-overlay-after-open')]/div[contains(@role,'dialog')]/div[contains(@class,'drawer-content vertical')]/div[contains(@class,'drawer-body')]/div[2]/div/div/div/div")
    update_industry=(By.XPATH,"//label[normalize-space()='Update industry']")
    done_button=(By.XPATH,"//button[normalize-space()='Done']")
    save_button=(By.XPATH,"//span[contains(text(),'Save')]")
    profile_button=(By.XPATH,"//div[contains(text(),'Profile')]")
    profile_picture=(By.XPATH,"//div[@class='upload cursor-pointer']")
    billing_button=(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]")
    security=(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]")
    first_name=(By.XPATH,"//input[contains(@placeholder,'First name')]")
    last_name=(By.XPATH,"//input[@placeholder='Last name']")
    submit=(By.XPATH,"//button[contains(@type,'submit')]")
    add_new_card=(By.XPATH,"//span[contains(text(),'Add new card')]")
    drawer_body=(By.XPATH,"//div[@class='drawer-body']")
    search_places=(By.XPATH,"//input[@placeholder='Search Places ...']")
    suggestion=(By.XPATH,"//span[normalize-space()='Vijay Nagar, Indore, Madhya Pradesh, India']")
    street_2=(By.XPATH,"//input[@placeholder='Floor no, APT no etc.']")
    upload_picture=(By.XPATH,"//div[@class='upload cursor-pointer']")
    update_button=(By.XPATH,"//button[normalize-space()='Update']")
    credit_card_number=(By.XPATH,"//input[@placeholder='•••• •••• •••• ••••']")
    exp_date=(By.XPATH,"//input[@placeholder='••/••']")
    cvv=(By.XPATH,"//input[@placeholder='•••']")
    switch_toggle=(By.XPATH,"//div[contains(@class,'switcher-toggle')]")
    forgot_button=(By.XPATH,"//button[normalize-space()='Forgot']")
    confirm_button=(By.XPATH,"//button[normalize-space()='Confirm']")
    user_name=(By.XPATH,"//input[@name='name']")
    send_otp=(By.XPATH,"//span[contains(text(),'Send OTP')]")

    def edit_company(self):
        self.click_on_account()
        self.click_on_profile()
        edit_image=self.EF.find_element(self.company_profile)
        edit_image.click()
        time.sleep(3)
        image_path=r"C:\Users\Quick\Desktop\Fruits_image.jpg"
        pyautogui.write(image_path)
        pyautogui.press('enter')
        time.sleep(3)
        edit_company_name=self.EF.find_element(self.company_name)
        edit_company_name.send_keys(Keys.BACKSPACE*60)
        edit_company_name.send_keys("AK Industries")
        edit_email=self.EF.find_element(self.email)
        edit_email.send_keys(Keys.BACKSPACE*150)
        edit_email.send_keys("ashu12@gmail.com")
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(0,100).perform()
        self.EF.find_element(self.flag_dropdown).click()
        self.EF.find_element(self.list_box)
        self.EF.find_element(self.search).send_keys("Ind")
        time.sleep(3)
        self.EF.find_element(self.country_name).click()
        edit_phone=self.EF.find_element(self.phone)
        edit_phone.send_keys(Keys.BACKSPACE*40)
        edit_phone.send_keys("912233445566")
        edit_role=self.EF.find_element(self.role)
        edit_role.send_keys(Keys.BACKSPACE*100)
        edit_role.send_keys("CEO")
        edit_bussiness_license=self.EF.find_element(self.business_license_number)
        edit_bussiness_license.send_keys(Keys.BACKSPACE*150)
        edit_bussiness_license.send_keys("12345")
        self.EF.find_element(self.insurance_number).send_keys("1029")
        self.EF.find_element(self.company_size).click()
        self.EF.find_element(self.business_years).click()
        self.EF.find_element(self.update_industry).click()
        categories_item=self.EF.find_elements(self.categories)
        for category in categories_item:
            category.click()
        self.EF.find_element(self.done_button).click()
        self.EF.find_element(self.send_otp).click()
        self.driver.close()

    def edit_user_profile(self):
        self.click_on_account()
        self.click_on_profile()
        self.EF.find_element(self.profile_button).click()
        edit_profile_picture=self.EF.find_element(self.profile_picture)
        edit_profile_picture.click()
        time.sleep(2)
        image_path=r"C:\Users\Quick\Desktop\profile_image.jpg"
        pyautogui.write(image_path)
        pyautogui.press('enter')
        time.sleep(3)
        edit_name=self.EF.find_element(self.first_name)
        edit_name.send_keys(Keys.BACKSPACE*30)
        edit_name.send_keys("Ashish")
        edit_last_name=self.EF.find_element(self.last_name)
        edit_last_name.send_keys(Keys.BACKSPACE*30)
        edit_last_name.send_keys("Khade")
        self.EF.find_element(self.submit).click()
        self.driver.close()

    def add_new_payment_card(self):
        self.click_on_account()
        self.click_on_profile()
        self.EF.find_element(self.billing_button).click()
        self.EF.find_element(self.add_new_card).click()
        self.EF.find_element(self.drawer_body)
        self.EF.find_element(self.search_places).send_keys("Vijay Nagar")
        self.EF.find_element(self.suggestion).click()
        self.EF.find_element(self.street_2).send_keys("First Floor")
        self.EF.find_element(self.user_name).send_keys("Ashish Khade")
        self.EF.find_element(self.credit_card_number).send_keys("4242424242424242")
        self.EF.find_element(self.exp_date).send_keys("12 20")
        self.EF.find_element(self.cvv).send_keys("123")
        image=self.EF.find_element(self.upload_picture)
        image.click()
        time.sleep(3)
        image_path=r"C:\Users\Quick\Desktop\profile_image.jpg"
        pyautogui.write(image_path)
        pyautogui.press('enter')
        time.sleep(3)
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(0,30).perform()
        self.EF.find_element(self.update_button).click()
        self.driver.close()







