from selenium.webdriver.common.by import By
from utility.elementry_function import Elem_Func

class Base:
    def __init__(self,driver):
        self.driver=driver
        self.EF=Elem_Func(self.driver)


    # def click_user_profile(self):

    # def click_logout_link(self):

    # def logout(self):
    #     self.click_user_profile()
    #     self.click_logout_link()

    # def navigate_to_tab(self,tab_link):





