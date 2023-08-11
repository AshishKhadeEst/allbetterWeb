from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Elem_Func:

    def __init__(self,driver):
        self.driver=driver

    def find_element(self,locator_tuple):
        try:
            element = WebDriverWait(self.driver, 10, poll_frequency=1).until(
                EC.element_to_be_clickable(locator_tuple))
            return element
        except:
            self.driver.save_screenshot('./reports/screenshots/failed_cases/failed_test.png')
            raise

    def mouse_hover(self, locator_tuple):
        element = self.find_element(locator_tuple)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

