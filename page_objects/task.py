from page_objects.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Add_Task(Base):

    add_task=(By.XPATH,"//span[@class='flex items-center justify-center']")
    add_client=(By.XPATH,"//span[contains(text(),'Add client')]")
    client_name=(By.XPATH,"//h6[normalize-space()='Ashish kumar khade']")
    address=(By.XPATH,"//span[contains(text(),'Nanda nagar street number 12 Third floor, Indore, ')]")
    task_title=(By.XPATH,"//input[@placeholder='Task Title']")
    task_description=(By.XPATH,"//textarea[@placeholder='Type here task description']")
    end_date=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]")
    datetime=(By.XPATH,"//div[@class='react-datepicker-popper']")
    date=(By.XPATH,"//div[@aria-label='Choose Wednesday, January 10th, 2024']")
    toggle=(By.XPATH,"//div[@class='switcher-toggle']")
    add_team=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]")
    name_client=(By.XPATH,"//label[@class='checkbox-label my-auto flex items-center flex-row-reverse w-full justify-between']")
    done=(By.XPATH,"//span[contains(text(),'Done')]")
    save_button=(By.XPATH,"//span[contains(text(),'Save')]")
    eye_symbol=(By.XPATH,"//tbody/tr[1]/td[6]/div[1]/div[1]")
    edit_button=(By.XPATH,"//span[contains(text(),'Edit')]")
    edit_start_date=(By.XPATH,"//input[@value='10/01/2024']")
    edit_end_date=(By.XPATH,"//input[@value='12/01/2024']")
    cross_button=(By.XPATH,"//span[@role='button']")
    change_property=(By.XPATH,"//span[contains(text(),'Change property')]")
    new_address=(By.XPATH,"//span[contains(text(),'Vijay Nagar Scheme No 54 Second floor, Indore, Mad')]")
    new_date=(By.XPATH,"//div[@aria-label='Choose Wednesday, January 10th, 2024']")
    action_button=(By.XPATH,"//span[contains(text(),'Action')]")
    mark_completed=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]")
    back_button=(By.XPATH,"//span[contains(text(),'Back')]")
    next_month=(By.XPATH,"//button[@aria-label='Next Month']")
    header=(By.XPATH,"//div[@class='react-datepicker__header ']")
    new_start_date=(By.XPATH,"//div[@aria-label='Choose Friday, January 12th, 2024']")
    start_time=(By.XPATH,"//input[@value='7:31 PM']")
    date_time_picker=(By.XPATH,"//div[@class='react-datepicker react-datepicker--time-only']")
    drawer=(By.XPATH,"//div[@class='drawer-content vertical']")

    def add_a_task(self):
        self.click_on_task()
        self.EF.find_element(self.add_task).click()
        self.EF.find_element(self.add_client).click()
        self.EF.find_element(self.client_name).click()
        self.EF.find_element(self.address).click()
        self.EF.find_element(self.task_title).send_keys("Test Task")
        self.EF.find_element(self.task_description).send_keys("No description")
        action=ActionChains(self.driver)
        action.scroll_by_amount(0,100).perform()
        self.EF.find_element(self.end_date).click()
        self.EF.find_element(self.datetime)
        self.EF.find_element(self.date).click()
        action.scroll_by_amount(0,100).perform()
        self.EF.find_element(self.toggle).click()
        self.EF.find_element(self.add_team).click()
        self.EF.find_element(self.name_client).click()
        self.EF.find_element(self.done).click()
        action.scroll_by_amount(0, 100).perform()
        self.EF.find_element(self.save_button).click()
        self.driver.close()

    def edit_task(self):
        self.click_on_task()
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10,100).perform()
        self.EF.find_element(self.eye_symbol).click()
        self.EF.find_element(self.edit_button).click()
        self.EF.find_element(self.change_property).click()
        self.EF.find_element(self.new_address).click()
        edit_title=self.EF.find_element(self.task_title)
        edit_title.send_keys(Keys.BACKSPACE*40)
        edit_title.send_keys("New Task")
        edit_description=self.EF.find_element(self.task_description)
        edit_description.send_keys(Keys.BACKSPACE*50)
        edit_description.send_keys("New description")
        actions.scroll_by_amount(10,100).perform()
        self.EF.find_element(self.edit_start_date).click()
        self.EF.find_element(self.datetime)
        self.EF.find_element(self.new_start_date).click()
        self.EF.find_element(self.edit_end_date).click()
        self.EF.find_element(self.datetime)
        self.EF.find_element(self.new_date).click()
        actions.scroll_by_amount(0,100).perform()
        self.EF.find_element(self.toggle).click()
        self.EF.find_element(self.add_team).click()
        self.EF.find_element(self.name_client).click()
        self.EF.find_element(self.done).click()
        self.EF.find_element(self.save_button).click()
        self.driver.close()

    def check_mark_completed(self):
        self.click_on_task()
        self.EF.find_element(self.eye_symbol).click()
        self.EF.find_element(self.action_button).click()
        self.EF.find_element(self.mark_completed).click()
        self.driver.close()

    def check_back_button(self):
        self.click_on_task()
        self.EF.find_element(self.add_task).click()
        self.EF.find_element(self.back_button).click()
        self.driver.close()










