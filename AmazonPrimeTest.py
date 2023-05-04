from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/anant/Downloads/chromedriver_win32 (2)/chromedriver.exe")

        self.driver.get("https://www.primevideo.com/offers/nonprimehomepage/ref=dvm_pds_amz_in_as_s_gm_16_mkw_symCJqBmk-dc?gclid=Cj0KCQjwr82iBhCuARIsAO0EAZzqECT8X7_LhbIAwkBNA6HvX5QFPpAAzyO_ZvFLd1xcSRJ-fCaRdtQaArcFEALw_wcB&mrntrk=pcrid_610141119783_slid__pgrid_84577172528_pgeo_9303346_x__adext__ptid_kwd-339065342343")

        self.driver.maximize_window()
    def test_login(self):
        driver = self.driver
        apname = '8534967541'
        apwd = 'Khurja@123'

        emailField = 'ap_email'
        pswdField = 'ap_password'
        loginBtnId = "signInSubmit"

        profileClassName = "nav-active-profile-name"

        driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[1]/div/div/div/div[2]/div[2]/div/ol/li[3]").click()
        driver.find_element_by_xpath('''//*[@id="pv-nav-container"]/div/div[2]/div[2]/div/ol/li[3]/div/div/ul/li[1]/a''').click()
        emailFieldElement = WebDriverWait(driver, 3).until(lambda driver: driver.find_element_by_id(emailField))
        passFieldElement = WebDriverWait(driver, 3).until(lambda driver: driver.find_element_by_id(pswdField))
        loginBtnElement = WebDriverWait(driver, 3).until(lambda driver: driver.find_element_by_id(loginBtnId))

        emailFieldElement.clear()
        emailFieldElement.send_keys(apname)
        passFieldElement.clear()
        passFieldElement.send_keys(apwd)
        loginBtnElement.click()
        profileElement = WebDriverWait(driver, 3).until(lambda driver: driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[1]/div/div/div/div[2]/div[2]/div/ol/li/label/div/span[1]"))
        self.assertIsNotNone(profileElement, "The result is not equal to none")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

