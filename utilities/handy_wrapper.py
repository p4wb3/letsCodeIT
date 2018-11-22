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
        elif locatorType in 'link_text':
            return By.LINK_TEXT
        else:
            print('locator types is not suported')
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