from selenium.webdriver.common.by import By


class HandyWraprer():

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