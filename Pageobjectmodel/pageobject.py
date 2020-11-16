import os
import time

from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

from basePage import BasePage
from pageLocators import MainPageLocators


class MainPage(BasePage):

    def __init__(self):
        self.MainPage_Locators = MainPageLocators()

    def check_page_loaded(self):
        return True if self.find_element_sub(*self.MainPage_Locators.LOGO) else False

    def set_companyname(self,comapnyname):
        self.find_element_sub(*self.MainPage_Locators.COMPANYNAME).send_keys(comapnyname)
        return True

    d
        finally:
            self.accept_next_alert = True


class HomePage(BasePage):
    pass

class SubmittedPageLocators(BasePage):
    pass