from page_objects.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Add_quotation(Base):

    add_quote=(By.XPATH,"//span[contains(@class,'flex items-center justify-center')]")
    add_client=(By.XPATH,"//span[contains(text(),'Add client')]")
    client=(By.XPATH,"//body[1]/div[10]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/h6[1]")
    address=(By.XPATH,"//span[contains(text(),'nagpur_road Ground Floor, Multai, Madhya Pradesh, ')]")
    description=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/textarea[1]")
    upload_file=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
    add_line_items=(By.XPATH,"//span[contains(text(),'Add line item')]")
    product=(By.XPATH,"//span[normalize-space()='product']")
    test_product=(By.XPATH,"//span[normalize-space()='Test product']")
    required_deposit=(By.XPATH,"//input[@placeholder='0.00']")
    client_message=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/textarea[1]")
    client_mess=(By.XPATH,"//div[contains(@class,'form-item vertical mt-4')]//div//textarea[contains(@type,'text')]")
    save=(By.XPATH,"//span[contains(text(),'Save')]")
    # location = "C:\Users\Quick\Downloads\Frame67.JPG"
    eye_symbol=(By.XPATH,"//tbody/tr[1]/td[6]/div[1]/div[1]//*[name()='svg']")
    edit_button=(By.XPATH,"//span[contains(text(),'Edit')]")
    new_item=(By.XPATH,"//span[normalize-space()='test test test test test test test test test']")
    tax=(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[3]/div[1]/div[2]/table[1]/tfoot[1]/tr[3]/td[2]/div[1]/div[1]/input[1]")
    collect_signature=(By.XPATH,"//canvas[@class='w-full']")
    save_signature=(By.XPATH,"//button[normalize-space()='Save']")
    next_button=(By.XPATH,"//button[normalize-space()='Next']")
    actions_button=(By.XPATH,"//span[contains(text(),'Action')]")
    approve_quote=(By.XPATH,"//span[normalize-space()='Approve Quote']")
    review_and_send=(By.XPATH,"//span[normalize-space()='Review and send']")
    sent_to=(By.XPATH,"//input[@name='to']")
    send_button=(By.XPATH,"//button[contains(@type,'submit')]")
    convert_to_job_button=(By.XPATH,"//span[normalize-space()='Convert to job']")
    job_title=(By.XPATH,"//input[contains(@placeholder,'Title')]")
    toggle=(By.XPATH,"//label[@class='switcher mr-2']")
    repeat_reminder=(By.XPATH,"//div[contains(text(),'Does not repeat')]")
    every_sunday=(By.XPATH,"//input[@id='react-select-101-input']")
    month=(By.XPATH,"//input[@id='react-select-104-input']")
    add_team=(By.XPATH,"//div[contains(@class,'flex justify-between items-center')]//button[contains(@type,'button')]")
    team_member=(By.XPATH,"//span[contains(text(),'John Dev')]")
    done=(By.XPATH,"//span[contains(text(),'Done')]")
    save_job=(By.XPATH,"//span[contains(text(),'Save')]")

    def add_quotation(self):
        self.click_on_quotation()
        self.EF.find_element(self.add_quote).click()
        self.EF.find_element(self.add_client).click()
        self.EF.find_element(self.client).click()
        self.EF.find_element(self.address).click()
        self.EF.find_element(self.description).send_keys("Add a quote")
        # self.EF.find_element(self.upload_file).send_keys("C:\Users\Quick\Downloads\Frame67.JPG")
        self.EF.find_element(self.add_line_items).click()
        self.EF.find_element(self.product).click()
        self.EF.find_element(self.test_product).click()
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(0,200).perform()
        self.EF.find_element(self.required_deposit).send_keys("100")
        self.EF.find_element(self.client_mess).send_keys("no message for client")
        self.EF.find_element(self.save).click()

    def edit_quote(self):
        self.click_on_quotation()
        self.EF.find_element(self.eye_symbol).click()
        self.EF.find_element(self.edit_button).click()
        edit_description=self.EF.find_element(self.description)
        edit_description.send_keys(Keys.BACKSPACE*40)
        edit_description.send_keys("Creating a quote through automation")
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(0,100).perform()
        self.EF.find_element(self.add_line_items).click()
        self.EF.find_element(self.new_item).click()
        actions.scroll_by_amount(0, 100).perform()
        self.EF.find_element(self.tax).send_keys("50")
        edit_deposit=self.EF.find_element(self.required_deposit)
        edit_deposit.send_keys(Keys.BACKSPACE*30)
        edit_deposit.send_keys("200")
        edit_client_message=self.EF.find_element(self.client_mess)
        edit_client_message.send_keys(Keys.BACKSPACE*50)
        edit_client_message.send_keys("Sending message through automation")
        self.EF.find_element(self.save).click()

    def approve_quotation(self):
        self.click_on_quotation()
        self.EF.find_element(self.eye_symbol).click()
        self.EF.find_element(self.actions_button).click()
        self.EF.find_element(self.approve_quote).click()
        self.EF.find_element(self.collect_signature).click()
        self.EF.find_element(self.save_signature).click()
        self.EF.find_element(self.next_button).click()

    def review_and_send_check(self,email):
        self.click_on_quotation()
        self.EF.find_element(self.eye_symbol).click()
        self.EF.find_element(self.actions_button).click()
        self.EF.find_element(self.review_and_send).click()
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(0,100).perform()
        self.EF.find_element(self.next_button).click()
        self.EF.find_element(self.sent_to).send_keys(email)
        self.EF.find_element(self.send_button).click()

    def convert_to_job(self):
        self.click_on_quotation()
        self.EF.find_element(self.eye_symbol).click()
        self.EF.find_element(self.actions_button).click()
        self.EF.find_element(self.convert_to_job_button).click()
        self.EF.find_element(self.job_title).send_keys("Test job")
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(0,100).perform()
        self.EF.find_element(self.repeat_reminder)
        # self.EF.find_element(self.every_sunday).click()
        # self.EF.find_element(self.month).click()
        self.EF.find_element(self.add_team).click()
        self.EF.find_element(self.team_member).click()
        actions.scroll_by_amount(0,100).perform()
        self.EF.find_element(self.done).click()
        self.EF.find_element(self.save_job).click()


















