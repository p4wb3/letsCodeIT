from traceback import print_stack

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time


class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self,locatorType ):
        locatorType  = locatorType.lower()
        if locatorType=='id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'linktext':
            return By.LINK_TEXT
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'classname':
            return By.CLASS_NAME
        else:
            print('locator' +locatorType+ 'is not correct/suported')
        return False

    def getEltment(self,locator, locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType )
            element =  self.driver.find_element(byType, locator)
            print('element found')
        except:
            print('element not found')
        return element

    def clickElement(self,locator,locatorType='id'):
        try:
            element = self.getEltment(locator, locatorType)
            element.click()
            print('Clicked on element with locator: '+ locator + ' locatorType: '+ locatorType)
        except:
            print('Cannot click on elementwith locator: '+ locator + ' locatorType: '+ locatorType)
            print_stack()

    def sendKeys(self,data,locator,locatorType='id'):
        try:
            element = self.getEltment(locator, locatorType)
            element.send_keys(data)
            print('Sent data on element with locator: '+ locator + ' locatorType: '+ locatorType)
        except:
            print('Cannot send data on elementwith locator: '+ locator + ' locatorType: '+ locatorType)
            print_stack()

    def isElementPresent(self, locator,byType):
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                print('element found')
                return True
            else:
                print('element not found')
                return False
        except:
            print('element not found')
            return False

    def elenentPresenceCheck(self,locator,byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) >0:
                print('element found')
                return True
            else:
                print('element not found')
                return False
        except:
            print('element not found')
            return False

    def expicitWait(self, locator, locatorType='id', timeout=10, pollFrequency= 0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
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

    def takeScreenshot(self):
        fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = 'F:\\letsCodeIt\\screenshots\\'
        destinationFile = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory --> :: " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")