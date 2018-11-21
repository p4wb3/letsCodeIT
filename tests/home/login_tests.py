from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from pages.home.login import LoginPage
class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        driverLocation = 'F:\\driver\\chromedriver.exe'
        baseURL = 'https://learn.letskodeit.com/'
        driver =  webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login('test@email.com','abcabc')



        userIcon = driver.find_element_by_xpath('//*[@id="navbar"]//span[text() ="Test User"]')
        if userIcon is not None:
            print('login Successful')
        else:
            print('Login Failed')



if __name__ == '__main__':
    unittest.main(verbosity=2)

