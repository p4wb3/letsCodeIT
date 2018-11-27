from utilities.handy_wrapper import HandyWraprer
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWait():

    def __init__(self,driver):
        self.driver = driver
        self.hw = HandyWraprer(driver)

    def ecpicitWait(self,locator,locatorType= 'id', timeout=10, pollFrequency= 0.5):
        element = None
        try:
            byType = self.hw.getByType(locatorType)
            print('Waiting for maximum::' + str(timeout) +
                  ':: seconds for element to be clickable ')
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])

            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            print('Element appered on the web page')
        except:
            print('Element not appered on the web page')
        return element
