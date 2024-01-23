from page_objects.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
class Add_client(Base):

    add_client=(By.XPATH,"//span[@class='flex items-center justify-center']")
    firs_name=(By.XPATH,"//input[@placeholder='First name']")
    last_name=(By.XPATH,"//input[@placeholder='Last name']")
    company=(By.XPATH,"//input[@placeholder='Company name (Optional)']")
    toggle=(By.XPATH,"//div[@class='switcher-toggle']")
    primary_phone=(By.XPATH,"//input[@value='+1']")
    secondary_number=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")
    search=(By.XPATH,"//input[@placeholder='search']")
    dropdown_1=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")
    flag=(By.XPATH,"//div[@class='selected-flag open']")
    listbox=(By.XPATH,"//ul[@role='listbox']")
    India=(By.XPATH,"//span[normalize-space()='India']")
    number=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
    number_2=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")
    dropdown_2=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]")
    USA=(By.XPATH,"//span[normalize-space()='United States']")
    email=(By.XPATH,"//input[@name='email']")
    secondary_email=(By.XPATH,"//input[@name='secondaryEmail']")
    search_places=(By.XPATH,"//input[@placeholder='Search Places ...']")
    street_1=(By.XPATH,"//input[@placeholder='Street 1']")
    street_2=(By.XPATH,"//input[@placeholder='Floor no, APT no etc.']")
    city=(By.XPATH,"//input[@placeholder='City']")
    state=(By.XPATH,"//input[@placeholder='State']")
    pstal_code=(By.XPATH,"//input[@placeholder='Postal code']")
    country=(By.XPATH,"//input[@placeholder='Country']")
    save=(By.XPATH,"//span[contains(text(),'Save')]")
    autoselect=(By.XPATH,"//span[contains(text(),'Vijay Nagar, Scheme No 54, Indore, Madhya Pradesh,')]")
    name=(By.XPATH,"(//span[contains(text(),'Ashish Khade')])[1]")
    edit_button=(By.XPATH,"//span[contains(text(),'Edit')]")
    autoselect_address=(By.XPATH,"//span[normalize-space()='Indira Gandhi ward, Multai, Madhya Pradesh, India']")
    back_button=(By.XPATH,"//span[contains(text(),'Back')]")
    search_box=(By.XPATH,"//input[@placeholder='Search...']")

    def add_a_client(self):
        self.click_on_client()
        self.EF.find_element(self.add_client).click()
        self.EF.find_element(self.firs_name).send_keys("Ashish")
        self.EF.find_element(self.last_name).send_keys("Khade")
        self.EF.find_element(self.company).send_keys("Khade Enterprises")
        self.EF.find_element(self.toggle).click()
        self.EF.find_element(self.primary_phone)
        self.EF.find_element(self.dropdown_1).click()
        self.EF.find_element(self.listbox)
        self.EF.find_element(self.search).click()
        self.EF.find_element(self.search).send_keys("Ind")
        self.EF.find_element(self.India).click()
        self.EF.find_element(self.number).send_keys("9893038093")
        self.EF.find_element(self.email).send_keys("ashishkhade@gmail.com")
        self.EF.find_element(self.secondary_number)
        self.EF.find_element(self.dropdown_2).click()
        self.EF.find_element(self.listbox)
        self.EF.find_element(self.search).click()
        self.EF.find_element(self.search).send_keys("Ind")
        self.EF.find_element(self.India).click()
        self.EF.find_element(self.number_2).send_keys("9893038093")
        self.EF.find_element(self.secondary_email).send_keys("ashishkhade11111@gmail.com")
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(10, 100).perform()
        self.EF.find_element(self.search_places).send_keys("Vijay nagar Indore")
        self.EF.find_element(self.autoselect).click()
        self.EF.find_element(self.street_2).send_keys("Second floor")
        self.EF.find_element(self.save).click()
        self.driver.close()

    def edit_client(self):
        self.click_on_client()
        self.EF.find_element(self.name).click()
        self.EF.find_element(self.edit_button).click()
        edit_first_name=self.EF.find_element(self.firs_name)
        edit_first_name.send_keys(Keys.BACKSPACE*10)
        edit_first_name.send_keys("Ashu")
        edit_last_name=self.EF.find_element(self.last_name)
        edit_last_name.send_keys(Keys.BACKSPACE*10)
        edit_last_name.send_keys("king")
        edit_company_name=self.EF.find_element(self.company)
        edit_company_name.send_keys(Keys.BACKSPACE*20)
        edit_company_name.send_keys("Test_Company")
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(20, 200).perform()
        time.sleep(3)
        self.EF.find_element(self.primary_phone)
        edit_primary_number=self.EF.find_element(self.number)
        edit_primary_number.send_keys(Keys.BACKSPACE*15)
        edit_primary_number.send_keys("917987273148")
        edit_primeary_eamil=self.EF.find_element(self.email)
        edit_primeary_eamil.send_keys(Keys.BACKSPACE*22)
        edit_primeary_eamil.send_keys("ashu123@gmail.com")
        actions.scroll_by_amount(10,200).perform()
        edit_address=self.EF.find_element(self.search_places)
        edit_address.send_keys("Indira Gandhi Ward Multai")
        self.EF.find_element(self.autoselect_address).click()
        self.EF.find_element(self.street_1).send_keys("nagpur_road")
        edit_street_2=self.EF.find_element(self.street_2)
        edit_street_2.send_keys(Keys.BACKSPACE*16)
        edit_street_2.send_keys("Ground Floor")
        self.EF.find_element(self.save).click()
        self.driver.close()

    def check_back_button(self):
        self.click_on_client()
        self.EF.find_element(self.name).click()
        self.EF.find_element(self.back_button).click()
        self.driver.close()

    def client_search_box(self,client_name):
        self.click_on_client()
        self.EF.find_element(self.search_box).send_keys(client_name)
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(10,100).perform()
        time.sleep(3)
        self.driver.close()


























