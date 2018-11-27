import time

from selenium import webdriver
from utilities.using_screenshot import Screenshots
from utilities.handy_wrapper import HandyWraprer

class UsingWrapper():

    def test(self):
        driverLocation = 'F:\\driver\\chromedriver.exe'
        baseUrl = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome(driverLocation)
        hw = HandyWraprer(driver)

        screenshot = Screenshots(driver)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)

        textField1 = hw.getEltment('name')
        textField1.send_keys('Test')
        time.sleep(2)
        textField2 = hw.getEltment('//input[@id="name"]','xPath')
        screenshot.takeScreenshot()
        textField2.clear()
ch = UsingWrapper()
ch.test()

