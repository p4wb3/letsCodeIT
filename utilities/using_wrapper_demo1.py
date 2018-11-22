import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handy_wrapper import HandyWraprer

class UsingWrapper():

    def test(self):
        driverLocation = 'F:\\driver\\chromedriver.exe'
        baseUrl = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome(driverLocation)
        hw = HandyWraprer(driver)

        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)

        textField1 = hw.getEltment('name')
        textField1.send_keys('Test')
        time.sleep(2)
        textField2 = hw.getEltment('//input[@id="name"]','xPath')
        textField2.clear()
ch = UsingWrapper()
ch.test()

