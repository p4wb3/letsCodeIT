from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locatars
    _login_link = 'Login'
    _email_field= 'user_email'
    _password_field ='user_password'
    _login_btn = 'commit'

    # def getLoginLink(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPasswordField(self):
    #     return  self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginBtn(self):
    #     return self.driver.find_element(By.NAME, self._login_btn)


    def clickLoginlink(self):
        self.clickElement(self._login_link, locatorType='link')


    def enterEmail(self,email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password,self._password_field)


    def clickLoginBtn(self):
        self.clickElement(self._login_btn, locatorType='name')


    def login(self, email, password):
        self.clickLoginlink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginBtn()

