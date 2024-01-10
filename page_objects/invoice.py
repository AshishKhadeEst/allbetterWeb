from page_objects.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Add_Invoice(Base):

    add_invoice=(By.XPATH,"//span[@class='flex items-center justify-center']")
    add_client=(By.XPATH,"//span[contains(text(),'Add client')]")
    client_name=(By.XPATH,"//h6[normalize-space()='Ashish kumar khade']")
    client_address=(By.XPATH,"//span[contains(text(),'Nanda nagar street number 12 Third floor, Indore, ')]")
    date=(By.XPATH,"//input[@value='07/01/2024']")
    datetime=(By.XPATH,"//div[@class='react-datepicker-popper']")
    select_date=(By.XPATH,"//div[@aria-label='Choose Wednesday, January 10th, 2024']")
    dropdown=(By.XPATH,"//div[@class='select-dropdown-indicator']")
    net=(By.ID,"react-select-43-live-region")
    add_line_items=(By.XPATH,"//span[contains(text(),'Add line item')]")
    service_name=(By.XPATH,"//span[normalize-space()='test test test test test test test test test']")
    product=(By.XPATH,"//span[normalize-space()='product']")
    product_name=(By.XPATH,"//span[normalize-space()='taxable product']")
    client_message=(By.XPATH,"//textarea[@placeholder='Type here your client message...']")
    save=(By.XPATH,"//span[contains(text(),'Save')]")
    eye_symbol=(By.XPATH,"//tbody/tr[1]/td[6]/div[1]/div[1]//*[name()='svg']")
    edit_button=(By.XPATH,"//span[contains(text(),'Edit')]")
    change_date=(By.XPATH,"//input[@value='27/06/2023']")
    next_month_button=(By.XPATH,"//button[@aria-label='Next Month']")
    next_date=(By.XPATH,"//div[@aria-label='Choose Tuesday, July 11th, 2023']")
    net_15=(By.XPATH,"//div[contains(text(),'Net 15')]")
    new_product=(By.XPATH,"//span[normalize-space()='Product 11123']")
    action_button=(By.XPATH,"//span[contains(text(),'Action')]")
    collect_deposite=(By.XPATH,"//span[normalize-space()='Collect deposite']")
    review_and_send=(By.XPATH,"//span[normalize-space()='Review and send']")
    collect_signature=(By.XPATH,"//span[normalize-space()='Collect signature']")
    notes=(By.XPATH,"//textarea[@placeholder='Notes']")
    next_button=(By.XPATH,"//button[normalize-space()='Next']")
    email=(By.XPATH,"//input[@name='to']")
    send_button=(By.XPATH,"//button[normalize-space()='Send']")
    signature_box=(By.XPATH,"//canvas[@class='w-full']")
    save_button=(By.XPATH,"//button[normalize-space()='Save']")
    save_signature=(By.XPATH,"//button[normalize-space()='Next']")
    eye_symbol_1=(By.XPATH,"//tbody/tr[3]/td[6]/div[1]/div[1]//*[name()='svg']")
    collect_deposite_button=(By.XPATH,"//button[normalize-space()='Collect deposite']")

    def add_a_invoice(self):
        self.click_on_invoice()
        self.EF.find_element(self.add_invoice).click()
        self.EF.find_element(self.add_client).click()
        self.EF.find_element(self.client_name).click()
        self.EF.find_element(self.client_address).click()
        self.EF.find_element(self.date).click()
        self.EF.find_element(self.datetime)
        self.EF.find_element(self.select_date).click()
        # self.EF.find_element(self.dropdown).click()
        # self.EF.find_element(self.net).click()
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(0,100).perform()
        self.EF.find_element(self.add_line_items).click()
        self.EF.find_element(self.service_name).click()
        self.EF.find_element(self.add_line_items).click()
        self.EF.find_element(self.product).click()
        self.EF.find_element(self.product_name).click()
        actions.scroll_by_amount(0,100).perform()
        self.EF.find_element(self.client_message).send_keys("No message now")
        self.EF.find_element(self.save).click()

    def edit_invoice(self):
        self.click_on_invoice()
        self.EF.find_element(self.eye_symbol).click()
        self.EF.find_element(self.edit_button).click()
        self.EF.find_element(self.change_date).click()
        self.EF.find_element(self.datetime)
        self.EF.find_element(self.next_month_button).click()
        self.EF.find_element(self.next_date).click()
        # self.EF.find_element(self.net_15).click()
        # self.EF.find_element(self.net).click()
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(0,100).perform()
        self.EF.find_element(self.add_line_items).click()
        self.EF.find_element(self.product).click()
        self.EF.find_element(self.new_product).click()
        actions.scroll_by_amount(0,200).perform()
        edit_client_message=self.EF.find_element(self.client_message)
        edit_client_message.send_keys(Keys.BACKSPACE*50)
        edit_client_message.send_keys("We have a invoice for you")
        self.EF.find_element(self.save).click()

    def check_collect_deposite(self):
        self.click_on_invoice()
        self.EF.find_element(self.eye_symbol_1).click()
        self.EF.find_element(self.action_button).click()
        self.EF.find_element(self.collect_deposite).click()
        self.EF.find_element(self.notes).send_keys("No comment")
        self.EF.find_element(self.collect_deposite_button).click()

    def check_review_and_send(self):
        self.click_on_invoice()
        self.EF.find_element(self.eye_symbol_1).click()
        self.EF.find_element(self.action_button).click()
        self.EF.find_element(self.review_and_send).click()
        self.EF.find_element(self.next_button).click()
        self.EF.find_element(self.email).send_keys("ashishkhade11@gmail.com")
        self.EF.find_element(self.send_button).click()

    def check_collect_signature(self):
        self.click_on_invoice()
        self.EF.find_element(self.eye_symbol_1).click()
        self.EF.find_element(self.action_button).click()
        self.EF.find_element(self.collect_signature).click()
        self.EF.find_element(self.signature_box).click()
        self.EF.find_element(self.save_button).click()
        self.EF.find_element(self.next_button).click()








