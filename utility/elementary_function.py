from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class Elem_Func:

    def __init__(self,driver):
        self.driver=driver

    def find_element(self,locator_tuple):
        try:
            element = WebDriverWait(self.driver, 10, poll_frequency=1).until(
                EC.element_to_be_clickable(locator_tuple))
            return element
        except:
            screenshot=self.driver.save_screenshot('./reports/screenshots/failed_cases/failed_test.png')
            return screenshot

    def mouse_hover(self, locator_tuple):
        element = self.find_element(locator_tuple)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def custom_logger():

            logger = logging.getLogger(__name__)
            logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s',
                                          datefmt='%d/%m/%Y %I:%M:%S')
            fh = logging.FileHandler(filename="Automation_log.log")
            fh.setFormatter(formatter)
            logger.addHandler(fh)
            return logger






