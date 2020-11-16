from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os
from pageLocators import *
from testCasesText import test_cases
from pageObjects import *


class TestPages(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        ff_profile = webdriver.FirefoxProfile()
        ff_profile.set_preference('browser.download.folderList',2)
        ff_profile.set_preference("browser.download.manager.showWhenStarting", False)
        ff_profile.set_preference("browser.download.dir", os.getcwd())
        ff_profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
        cls.driver = webdriver.Firefox(firefox_profile=ff_profile)

        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
        cls.base_url = ("https://hudson-poutine-83447.herokuapp.com/")
        cls.driver.get(cls.base_url)
        cls.main_page = MainPage(cls.driver)

    def test_page_load(self):
        print "\n" + str(test_cases(0))
        #page = MainPage(self.driver)
        self.assertTrue(self.main_page.check_page_loaded())

    def test_set_comapanyname(self):
        print "\n" + str(test_cases(1))
        self.assertTrue(self.main_page.set_comapnyname('Victor'),'Failed to set companyname')



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestPages('test_page_load'))
    suite.addTest(TestPages('test_companyname'))

    #run test in the added rder, otherwise it will be alphabetical order
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

    #suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    #unittest.main(verbosity=2)