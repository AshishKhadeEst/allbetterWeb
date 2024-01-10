from utility.elementary_function import Elem_Func
from selenium.webdriver.common.by import By

class Base:

    def __init__(self, driver):
        self.driver = driver
        self.EF = Elem_Func(self.driver)

    client = (By.XPATH, "//span[normalize-space()='Client']")
    requests = (By.XPATH,"//span[normalize-space()='Request']")
    quotation = (By.XPATH,"//span[normalize-space()='Quotation']")
    job = (By.XPATH,"//span[normalize-space()='Job']")
    invoice = (By.XPATH,"//span[normalize-space()='Invoice']")
    task = (By.XPATH,"//span[normalize-space()='Task']")
    crm_button=(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/nav[1]/div[2]/ul[1]/div[1]/div[1]")
    notes=(By.XPATH,"//span[normalize-space()='Notes']")
    settings=(By.XPATH,"//span[contains(text(),'Settings')]")
    employees=(By.XPATH,"//span[normalize-space()='Employees']")
    product_and_services=(By.XPATH,"//span[normalize-space()='Products & Services']")

    def click_on_client(self):
        self.EF.find_element(self.client).click()

    def click_on_request(self):
        self.EF.find_element(self.requests).click()

    def click_on_quotation(self):
        self.EF.find_element(self.quotation).click()

    def click_on_job(self):
        self.EF.find_element(self.job).click()

    def click_on_invoice(self):
        self.EF.find_element(self.invoice).click()

    def click_on_task(self):
        self.EF.find_element(self.task).click()

    def click_on_notes(self):
        self.EF.find_element(self.notes).click()

    def click_on_crm(self):
        self.EF.find_element(self.crm_button).click()


