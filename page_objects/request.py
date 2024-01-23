from page_objects.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
class Add_request(Base):

    Add_request_button= (By.XPATH,"//span[contains(@class,'flex items-center justify-center')]")
    add_client = (By.XPATH,"//span[contains(text(),'Add client')]")
    name= (By.XPATH,"//body[1]/div[10]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]")
    address= (By.XPATH,"//div[@class='card-body']")
    description= (By.XPATH,"//div[@class='form-item vertical']//div//textarea[@type='text']")
    add_team= (By.XPATH,"//span[@class='ltr:ml-1 rtl:mr-1'][normalize-space()='Add']")
    team_member_1= (By.XPATH,"//span[contains(text(),'Captain Jack sparrow')]")
    team_member_2= (By.XPATH,"//span[contains(text(),'John Dev')]")
    done= (By.XPATH,"//span[contains(text(),'Done')]")
    service_details=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/textarea[1]")
    request_instructions= (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/textarea[1]")
    next_month= (By.XPATH,"//button[@aria-label='Next Month']")
    calendar= (By.XPATH,"//div[@class='react-datepicker__month-container']")
    date_1= (By.XPATH,"//div[@aria-label='Choose Tuesday, January 16th, 2024']")
    start_time=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")
    time_picker=(By.XPATH,"//div[@class='react-datepicker react-datepicker--time-only']")
    start_time_select=(By.XPATH,"//li[normalize-space()='12:00 AM']")
    end_time_select=(By.XPATH,"//li[normalize-space()='1:15 AM']")
    end_time= (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]")
    morning= (By.XPATH,"//input[@value='morning']")
    save= (By.XPATH,"//span[contains(text(),'Save')]")
    schedule=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
    eye_click=(By.XPATH,"//tbody/tr[7]/td[6]/div[1]/div[1]//*[name()='svg']")
    edit_button=(By.XPATH,"//span[contains(text(),'Edit')]")
    change_property=(By.XPATH,"//span[contains(text(),'Change property')]")
    Add_address=(By.XPATH,"//span[contains(text(),'Add address')]")
    search_places=(By.XPATH,"//input[contains(@placeholder,'Search Places ...')]")
    autosuggestion = (By.XPATH, "//span[normalize-space()='Vijay Nagar, Indore, Madhya Pradesh, India']")
    floor_2 = (By.XPATH, "//input[@placeholder='Floor no, APT no etc.']")
    save_address = (By.XPATH, "//span[contains(text(),'Save address')]")
    new_address = (By.XPATH, "//span[contains(text(),'Vijay Nagar , Indore, Madhya Pradesh, India, 452010')]")
    add_team_member=(By.XPATH,"//div[@class='drawer-portal']//div[4]//label[1]")
    new_date=(By.XPATH,"//div[@aria-label='Choose Tuesday, December 26th, 2023']")
    visit_time=(By.XPATH,"//input[contains(@value,'noon')]")
    search_option=(By.XPATH,"//input[@placeholder='Search...']")
    all_options=(By.XPATH,"//div[contains(text(),'All')]")
    completed=(By.XPATH,"//input[@id='react-select-14-input']")
    archived=(By.XPATH,"//input[@id='react-select-14-input']")
    pending=(By.XPATH,"//input[@id='react-select-14-input']")
    converted=(By.XPATH,"//input[@id='react-select-14-input']")
    actions=(By.XPATH,"//span[contains(text(),'Action')]")
    mark_complete=(By.XPATH,"//span[normalize-space()='Mark complete']")
    convert_to_quote=(By.XPATH,"//span[normalize-space()='Convert to quote']")
    convert_to_job=(By.XPATH,"//span[normalize-space()='Convert to job']")
    archive=(By.XPATH,"//span[normalize-space()='Archive']")
    add_line_items=(By.XPATH,"//span[contains(text(),'Add line item')]")
    cleaners=(By.XPATH,"//span[normalize-space()='Cleaners']")
    required_deposite=(By.XPATH,"//input[@placeholder='0.00']")
    client_message=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/textarea[1]")
    save_b=(By.XPATH,"//span[contains(text(),'Save')]")
    title=(By.XPATH,"//input[@placeholder='Title']")

    def add_request(self):
        self.click_on_request()
        self.EF.find_element(self.Add_request_button).click()
        self.EF.find_element(self.add_client).click()
        self.EF.find_element(self.name).click()
        self.EF.find_element(self.address).click()
        self.EF.find_element(self.description).send_keys("No description required")
        self.EF.find_element(self.add_team).click()
        self.EF.find_element(self.team_member_2).click()
        self.EF.find_element(self.team_member_1).click()
        self.EF.find_element(self.done).click()
        self.EF.find_element(self.request_instructions).send_keys("No instructions now")
        self.EF.find_element(self.service_details).send_keys("need a cleaning team")
        self.EF.find_element(self.schedule).click()
        self.EF.find_element(self.next_month).click()
        self.EF.find_element(self.calendar)
        self.EF.find_element(self.date_1).click()
        self.EF.find_element(self.start_time).click()
        self.EF.find_element(self.time_picker)
        self.EF.find_element(self.start_time_select).click()
        self.EF.find_element(self.end_time).click()
        self.EF.find_element(self.time_picker)
        self.EF.find_element(self.end_time_select).click()
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(0,100).perform()
        self.EF.find_element(self.morning).click()
        self.EF.find_element(self.save).click()
        self.driver.close()

    def edit_request(self):
        self.click_on_request()
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(0, 200).perform()
        self.EF.find_element(self.eye_click).click()
        self.EF.find_element(self.edit_button).click()
        edit_description=self.EF.find_element(self.description)
        edit_description.send_keys(Keys.BACKSPACE*40)
        edit_description.send_keys("No description for now")
        self.EF.find_element(self.add_team).click()
        self.EF.find_element(self.add_team_member).click()
        self.EF.find_element(self.done).click()
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(0,200).perform()
        edit_instructions=self.EF.find_element(self.request_instructions)
        edit_instructions.send_keys(Keys.BACKSPACE*50)
        edit_instructions.send_keys("Need a solid team")
        edit_services=self.EF.find_element(self.service_details)
        edit_services.send_keys(Keys.BACKSPACE*50)
        edit_services.send_keys("We have a very good cleaning team")
        self.EF.find_element(self.schedule).click()
        self.EF.find_element(self.calendar)
        self.EF.find_element(self.next_month).click()
        self.EF.find_element(self.next_month).click()
        self.EF.find_element(self.next_month).click()
        self.EF.find_element(self.new_date).click()
        self.EF.find_element(self.visit_time).click()
        self.EF.find_element(self.save).click()
        self.driver.close()

    def check_search(self,client_name):
        self.click_on_request()
        self.EF.find_element(self.search_option).send_keys(client_name)
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(0,300).perform()
        self.driver.close()

    def check_filter(self):
        self.click_on_request()
        self.EF.find_element(self.all_options).click()
        self.EF.find_element(self.completed).click()
        self.EF.find_element(self.all_options).click()
        self.EF.find_element(self.pending).click()
        self.EF.find_element(self.all_options).click()
        self.EF.find_element(self.archived).click()
        self.EF.find_element(self.all_options).click()
        self.EF.find_element(self.converted).click()
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(0,100).perform()
        self.driver.close()

    def check_convert_to_quote(self):
        self.click_on_request()
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(0, 200).perform()
        self.EF.find_element(self.eye_click).click()
        self.EF.find_element(self.actions).click()
        self.EF.find_element(self.convert_to_quote).click()
        edit_description=self.EF.find_element(self.description)
        edit_description.send_keys(Keys.BACKSPACE*60)
        edit_description.send_keys("Add a quote")
        actions.scroll_by_amount(0,200).perform()
        self.EF.find_element(self.add_line_items).click()
        self.EF.find_element(self.cleaners).click()
        self.EF.find_element(self.required_deposite).send_keys("100")
        actions.scroll_by_amount(0,100).perform()
        self.EF.find_element(self.client_message).click()
        self.EF.find_element(self.save_b).click()
        self.driver.close()

    def check_convert_to_job(self):
        self.click_on_request()
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(0, 200).perform()
        self.EF.find_element(self.eye_click).click()
        self.EF.find_element(self.actions).click()
        self.EF.find_element(self.convert_to_job).click()
        self.EF.find_element(self.title).send_keys("Test job")
        actions.scroll_by_amount(0,200).perform()
        self.EF.find_element(self.add_line_items).click()
        self.EF.find_element(self.cleaners).click()
        self.EF.find_element(self.save_b).click()
        self.driver.close()

    def check_archieve(self):
        self.click_on_request()
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(0, 200).perform()
        self.EF.find_element(self.eye_click).click()
        self.EF.find_element(self.actions).click()
        self.EF.find_element(self.archived).click()
        self.driver.close()

    def check_request_completed(self):
        self.click_on_request()
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(0, 200).perform()
        self.EF.find_element(self.eye_click).click()
        self.EF.find_element(self.actions).click()
        self.EF.find_element(self.mark_complete).click()
        self.driver.close()
























