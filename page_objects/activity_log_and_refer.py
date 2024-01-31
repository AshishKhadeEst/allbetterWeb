from page_objects.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Action_Log_Refer(Base):

    eye_symbol_1=(By.XPATH,"//tbody/tr[1]/td[5]/div[1]/div[1]")
    back_button=(By.XPATH,"//span[contains(text(),'Back')]")
    eye_symbol_2=(By.XPATH,"//tbody/tr[2]/td[5]/div[1]/div[1]")
    all_buttons=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[2]/button")

    def check_activity(self):
        self.click_on_account()
        self.click_on_activity_logs()
        self.EF.find_element(self.eye_symbol_1).click()
        self.EF.find_element(self.back_button).click()
        self.EF.find_element(self.eye_symbol_2).click()
        self.EF.find_element(self.back_button).click()
        self.driver.close()

    def check_referral(self):
        self.click_on_account()
        self.click_on_refer_a_friend()
        buttons=self.EF.find_elements(self.all_buttons)
        for button in buttons:
            button.click()
        self.driver.close()







