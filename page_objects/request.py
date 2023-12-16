from page_objects.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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
    date_1= (By.XPATH,"//div[@aria-label='Choose Saturday, December 30th, 2023']")
    start_time=(By.XPATH,"")
    time_picker=(By.XPATH,"//div[@class='react-datepicker-popper']")
    start_time_select=(By.XPATH,"//li[normalize-space()='8:40 PM']")
    end_time_select=(By.XPATH,"////li[normalize-space()='10:30 PM']")
    end_time= (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]")
    morning= (By.XPATH,"//input[@value='morning']")
    save= (By.XPATH,"//span[contains(text(),'Save')]")
    schedule=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")

    def add_request(self):
        self.click_on_request()
        self.EF.find_element(self.Add_request_button).click()
        self.EF.find_element(self.add_client).click()
        self.EF.find_element(self.name).click()
        self.EF.find_element(self.address).click()
        self.EF.find_element(self.description).click()
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
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(0,10).perform()
        self.EF.find_element(self.start_time_select).clcik()
        self.EF.find_element(self.end_time).click()
        self.EF.find_element(self.time_picker)
        self.EF.find_element(self.end_time_select).click()
        self.EF.find_element(self.morning).click()
        self.EF.find_element(self.save).click()








