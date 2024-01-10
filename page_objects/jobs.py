from page_objects.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Add_job(Base):

    add_job=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[2]/div[3]/button[1]")
    job_title=(By.XPATH,"//input[contains(@placeholder,'Title')]")
    message=(By.XPATH,"//textarea[@placeholder='Type here your client message...']")
    date=(By.XPATH,"//input[contains(@placeholder,'2023-12-25')]")
    date_picker=(By.XPATH,"//div[@class='react-datepicker']")
    select_date=(By.XPATH,"//div[@aria-label='Choose Saturday, December 30th, 2023']")
    select_team=(By.XPATH,"//div[@class='flex justify-between items-center']//button[@type='button']")
    team_member_1=(By.XPATH,"//span[contains(text(),'John Dev')]")
    team_member_2=(By.XPATH,"//span[contains(text(),'Captain Jack sparrow')]")
    done=(By.XPATH,"//div[contains(@class,'text-end')]//span[contains(@class,'flex items-center justify-center')]")
    add_line_items=(By.XPATH,"//span[contains(text(),'Add line item')]")
    product=(By.XPATH,"//span[normalize-space()='product']")
    taxable_product=(By.XPATH,"//span[normalize-space()='taxable product']")
    save_button=(By.XPATH,"//span[contains(text(),'Save')]")
    add_client=(By.XPATH,"//span[contains(text(),'Add client')]")
    client_name=(By.XPATH,"//h6[normalize-space()='Ashish kumar khade']")
    drawer_body=(By.XPATH,"//div[@class='drawer-content vertical']")
    address=(By.XPATH,"//div[@class='card-body']")
    toggle=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/label[1]")
    add_a_new_client=(By.XPATH,"/html[1]/body[1]/div[11]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]")
    first_name=(By.XPATH,"//input[@placeholder='First name']")
    last_name=(By.XPATH,"//input[@placeholder='Last name']")
    primary_phone=(By.XPATH,"//body[1]/div[11]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
    flag=(By.XPATH,"//div[contains(@class,'selected-flag open')]")
    list_box=(By.XPATH,"//ul[@role='listbox']")
    search=(By.XPATH,"//input[@placeholder='search']")
    india=(By.XPATH,"//span[normalize-space()='India']")
    input_box=(By.XPATH,"//input[contains(@value,'+91')]")
    email=(By.XPATH,"//input[@name='email']")
    search_places=(By.XPATH,"//input[@placeholder='Search Places ...']")
    street_1=(By.XPATH,"//input[@placeholder='Street 1']")
    city=(By.XPATH,"//input[@placeholder='City']")
    state=(By.XPATH,"//input[@placeholder='State']")
    post_code=(By.XPATH,"//input[@placeholder='Postal code']")
    country=(By.XPATH,"//input[@placeholder='Country']")
    save=(By.XPATH,"//div[@class='drawer-body']//form[@action='#']//button[@type='submit']")
    repeat_reminder=(By.XPATH,"//div[@class='select__single-value css-glxgzj-singleValue']")
    eye_symbol=(By.XPATH,"//tbody/tr[1]/td[6]/div[1]/div[1]//*[name()='svg']")
    edit_button=(By.XPATH,"//span[contains(text(),'Edit')]")
    movers=(By.XPATH,"//span[normalize-space()='Movers']")
    update=(By.XPATH,"//span[contains(text(),'Update')]")
    actions=(By.XPATH,"//span[contains(text(),'Action')]")
    job_completed=(By.XPATH,"//span[normalize-space()='Mark Job Complete']")
    collect_signature=(By.XPATH,"//span[normalize-space()='Collect signature']")
    text_field=(By.XPATH,"/html[1]/body[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/canvas[1]")
    save_b=(By.XPATH,"//button[normalize-space()='Save']")
    next_button=(By.XPATH,"//button[normalize-space()='Next']")
    back_button=(By.XPATH,"//span[contains(text(),'Back')]")

    def create_job(self):
        self.click_on_job()
        self.EF.find_element(self.add_job).click()
        self.EF.find_element(self.add_client).click()
        self.EF.find_element(self.drawer_body)
        self.EF.find_element(self.client_name).click()
        self.EF.find_element(self.address).click()
        self.EF.find_element(self.job_title).send_keys("Automaton testing")
        self.EF.find_element(self.message).send_keys("No message for client")
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(0,100).perform()
        self.EF.find_element(self.date).click()
        self.EF.find_element(self.date_picker)
        self.EF.find_element(self.select_date).click()
        self.EF.find_element(self.toggle).click()
        actions.scroll_by_amount(0,500).perform()
        self.EF.find_element(self.repeat_reminder)
        self.EF.find_element(self.select_team).click()
        self.EF.find_element(self.team_member_1).click()
        self.EF.find_element(self.team_member_2).click()
        self.EF.find_element(self.done).click()
        self.EF.find_element(self.add_line_items).click()
        self.EF.find_element(self.product).click()
        self.EF.find_element(self.taxable_product).click()
        self.EF.find_element(self.save_button).click()

    def edit_job(self):
        self.click_on_job()
        self.EF.find_element(self.eye_symbol).click()
        self.EF.find_element(self.edit_button).click()
        edit_title=self.EF.find_element(self.job_title)
        edit_title.send_keys(Keys.BACKSPACE*40)
        edit_title.send_keys("Test job")
        job_description=self.EF.find_element(self.message)
        job_description.send_keys(Keys.BACKSPACE*50)
        job_description.send_keys("No message for now")
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(10,100).perform()
        self.EF.find_element(self.add_line_items).click()
        self.EF.find_element(self.movers).click()
        self.EF.find_element(self.update).click()

    def collect_the_signature(self):
        self.click_on_job()
        self.EF.find_element(self.eye_symbol).click()
        self.EF.find_element(self.actions).click()
        self.EF.find_element(self.collect_signature).click()
        self.EF.find_element(self.text_field).click()
        self.EF.find_element(self.save_b).click()
        self.EF.find_element(self.next_button).click()

    def complete_job(self):
        self.click_on_job()
        self.EF.find_element(self.eye_symbol).click()
        self.EF.find_element(self.actions).click()
        self.EF.find_element(self.job_completed).click()

    def check_back_button(self):
        self.click_on_job()
        self.EF.find_element(self.eye_symbol).click()
        self.EF.find_element(self.back_button).click()











