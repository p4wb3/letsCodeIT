import time


class Screenshots():
    def __init__(self,driver):
        self.driver = driver

    def takeScreenshot(self):
        """
        Takes screenshot of the current open web page
        :param driver
        :return:
        """
        fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = 'F:\\letsCodeIt\\screenshots\\'
        destinationFile = screenshotDirectory + fileName

        try:
            self.driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory --> :: " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")