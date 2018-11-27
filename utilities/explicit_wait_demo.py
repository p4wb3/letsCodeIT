from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.using_explicit_wait import ExplicitWait

class ExplicitWaitDemo():
    def test(self):
        driverLocation = 'F:\\driver\\chromedriver.exe'
        baseUrl = 'http:/www.expedia.com'
        driver = webdriver.Chrome(driverLocation)
        driver.implicitly_wait(.5)
        driver.maximize_window()
        wait = ExplicitWait(driver)
        driver.get(baseUrl)
        driver.find_element(By.ID, 'tab-flight-tab-hp').click()
        driver.find_element(By.ID, 'flight-origin-hp-flight').send_keys('SFO')
        driver.find_element(By.ID, 'flight-destination-hp-flight').send_keys('NYC')
        driver.find_element(By.ID, 'flight-departing-hp-flight').send_keys('12/21/2018')
        returnDate = driver.find_element(By.ID, 'flight-returning-hp-flight')
        returnDate.clear()
        time.sleep(.5)
        returnDate.send_keys('12/27/2018')
        driver.find_element(By.XPATH, "//form[@id='gcw-flights-form-hp-flight']//button[@type='submit']").click()
        # driver.find_element(By.ID, 'Nonstop-stop-flights-checkbox').click()

        element = wait.ecpicitWait('stops')
        element.click()

        time.sleep(2)
        driver.quit()

ch = ExplicitWaitDemo()
ch.test()