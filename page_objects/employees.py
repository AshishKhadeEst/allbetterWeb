from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from page_objects.base import Base

class Add_Employees(Base):

    add_employees=(By.XPATH,"//span[@class='flex items-center justify-center']")
