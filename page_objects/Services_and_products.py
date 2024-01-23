from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from page_objects.base import Base

class Product_And_Services(Base):

    add_line_items=(By.XPATH,"//span[@class='flex items-center justify-center']")
    title=(By.XPATH,"//input[@placeholder='Title']")
    description=(By.XPATH,"//textarea[@placeholder='Description']")
    unit_price=(By.XPATH,"//input[@placeholder='0.00']")
    exempt_tax=(By.XPATH,"//input[@name='exemptFromTax']")
    save_button=(By.XPATH,"//span[contains(text(),'Save')]")
    product_button=(By.XPATH,"//input[@value='product']")
    service_button=(By.XPATH,"//input[@value='service']")
    quantity=(By.XPATH,"//input[@placeholder='Quantity']")
    edit_button=(By.XPATH,"//tbody/tr[2]/td[7]/div[1]/div[1]")

    def add_service(self):
        self.click_on_settings()
        self.click_on_product_and_services()
        self.EF.find_element(self.add_line_items).click()
        self.EF.find_element(self.title).send_keys("Movers_Hub")
        self.EF.find_element(self.description).send_keys("No description for now")
        self.EF.find_element(self.unit_price).send_keys("100")
        self.EF.find_element(self.exempt_tax).click()
        self.EF.find_element(self.save_button).click()
        self.driver.close()

    def add_products(self):
        self.click_on_settings()
        self.click_on_product_and_services()
        self.EF.find_element(self.add_line_items).click()
        self.EF.find_element(self.product_button).click()
        self.EF.find_element(self.title).send_keys("New Product")
        self.EF.find_element(self.description).send_keys("New product description")
        qty=self.EF.find_element(self.quantity)
        qty.clear()
        qty.send_keys("10")
        self.EF.find_element(self.unit_price).send_keys("500")
        self.EF.find_element(self.exempt_tax).click()
        self.EF.find_element(self.save_button).click()
        self.driver.close()

    def edit_product(self):
        self.click_on_settings()
        self.click_on_product_and_services()
        self.EF.find_element(self.edit_button).click()
        self.EF.find_element(self.service_button).click()
        edit_title=self.EF.find_element(self.title)
        edit_title.send_keys(Keys.BACKSPACE*100)
        edit_title.send_keys("New service")
        edit_description=self.EF.find_element(self.description)
        edit_description.send_keys(Keys.BACKSPACE*150)
        edit_description.send_keys("No description")
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(0,100).perform()
        edit_unit_price=self.EF.find_element(self.unit_price)
        edit_unit_price.send_keys(Keys.BACKSPACE*100)
        edit_unit_price.send_keys("2000")
        self.EF.find_element(self.exempt_tax).click()
        self.EF.find_element(self.save_button).click()
        self.driver.close()


















