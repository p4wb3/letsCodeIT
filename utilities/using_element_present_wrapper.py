from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.handy_wrapper import HandyWraprer


class ElementPresentCheck():
    driverLocation = 'F:\\driver\\chromedriver.exe'
    baseUrl = 'https://learn.letskodeit.com/p/practice'
    driver = webdriver.Chrome(driverLocation)
    hw = HandyWraprer(driver)
    driver.get(baseUrl)

    elementResult1 = hw.isElementPresent('name',By.ID)
    print(str(elementResult1))

    elementResult2 = hw.elenentPresenceCheck('//input[@id = "name"]', By.XPATH)
    print(str(elementResult2))