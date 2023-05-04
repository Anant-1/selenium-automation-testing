from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/anant/Downloads/chromedriver_win32 (2)/chromedriver.exe")
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()
    def test_login(self):
        driver = self.driver
        fbname = '8534967541'
        fpwd = 'Anant@768'

        emailField = 'email'
        pswdField = 'pass'
        loginBtnName = "login"
        myName = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a/div[1]/div[2]/div/div/div/div/span/span"

        emailFieldElement = WebDriverWait(driver, 3).until(lambda driver: driver.find_element_by_id(emailField))
        passFieldElement = WebDriverWait(driver, 3).until(lambda driver: driver.find_element_by_id(pswdField))
        loginBtnElement = WebDriverWait(driver, 3).until(lambda driver: driver.find_element_by_name(loginBtnName))

        emailFieldElement.clear()
        emailFieldElement.send_keys(fbname)
        passFieldElement.clear()
        passFieldElement.send_keys(fpwd)
        loginBtnElement.click()
        WebDriverWait(driver, 3).until(lambda driver: driver.find_element_by_xpath(myName))
        

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
