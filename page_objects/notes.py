import time
from page_objects.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui

class Add_Notes(Base):

    add_note=(By.XPATH,"//span[@class='flex items-center justify-center']")
    add_client=(By.XPATH,"//span[contains(text(),'Add client')]")
    client_name=(By.XPATH,"//h6[normalize-space()='Ashish kumar khade']")
    address=(By.XPATH,"//span[contains(text(),'Nanda nagar street number 12 Third floor, Indore, ')]")
    description=(By.XPATH,"//textarea[@placeholder='Type notes here']")
    file_upload=(By.XPATH,"//div[@class='upload upload-draggable hover:border-indigo-600 min-h-fit']")
    quote=(By.XPATH,"//span[normalize-space()='Quote']")
    requests=(By.XPATH,"//span[normalize-space()='Request']")
    job=(By.XPATH,"//span[normalize-space()='Job']")
    invoice=(By.XPATH,"//span[normalize-space()='Invoice']")
    task = (By.XPATH,"//span[normalize-space()='Task']")
    save_button=(By.XPATH,"//span[contains(text(),'Save')]")
    eye_symbol=(By.XPATH,"//tbody/tr[1]/td[5]/div[1]/div[1]")
    edit=(By.XPATH,"//span[contains(text(),'Edit')]")

    def add_notes(self):
        self.click_on_crm()
        self.click_on_notes()
        self.EF.find_element(self.add_note).click()
        self.EF.find_element(self.add_client).click()
        self.EF.find_element(self.client_name).click()
        self.EF.find_element(self.address).click()
        self.EF.find_element(self.description).send_keys("Adding a new notes through automation")
        input_files=self.EF.find_element(self.file_upload)
        image_path=r'C:\Users\Quick\Desktop\profile_image.jpg'
        input_files.click()
        time.sleep(3)
        pyautogui.write(image_path)
        pyautogui.press('enter')
        time.sleep(3)
        self.EF.find_element(self.quote).click()
        self.EF.find_element(self.requests).click()
        self.EF.find_element(self.job).click()
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(0,100).perform()
        self.EF.find_element(self.save_button).click()
        self.driver.close()

    def edit_notes(self):
        self.click_on_crm()
        self.click_on_notes()
        self.EF.find_element(self.eye_symbol).click()
        self.EF.find_element(self.edit).click()
        edit_description=self.EF.find_element(self.description)
        edit_description.send_keys(Keys.BACKSPACE*60)
        edit_description.send_keys("New description for the notes")
        input_files = self.EF.find_element(self.file_upload)
        image_path = r'C:\Users\Quick\Desktop\profile_image.jpg'
        input_files.click()
        time.sleep(3)
        pyautogui.write(image_path)
        pyautogui.press('enter')
        self.EF.find_element(self.quote).click()
        self.EF.find_element(self.task).click()
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(0,100).perform()
        self.EF.find_element(self.save_button).click()
        self.driver.close()









