import selenium.webdriver.support.expected_conditions as WAITCON
import random
import string
import time
import inspect

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from toolium.pageelements import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from toolium.pageelements import InputText, Button
from toolium.pageobjects.page_object import PageObject
####################################################################

from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
from pageobjects.message import MessagePageObject
from pageobjects.secure_area import SecureAreaPageObject

class CandidatesPageObject(PageObject):
    def init_page_elements(self):
        self.username = InputText(By.NAME, 'txtUsername')
        self.password = InputText(By.NAME, 'txtPassword')
        self.login_button = Button(By.XPATH, '//*[@id="btnLogin"]')

        self.message = MessagePageObject()



    def open(self):
        """ Open login url in browser

        :returns: this page object instance
        """
        self.driver.get('{}/submit'.format(self.config.get('Test', 'url')))
        return self

    def wait_until_loaded(self):
        """ Wait until login page is loaded

        :returns: this page object instance
        """
        self.username.wait_until_visible()
        return self

    def login(self, user):
        """ Fill login form and submit it

        :param user: dict with username and password values
        :returns: secure area page object instance
        """
        #self.logger.debug("Login with user '%s'", user['username'])
        self.username.text = user['username']
        self.password.text = user['password']
        time.sleep(3)
        self.login_button.click()
        time.sleep(3)

        return self

    def hover(self):
        self.element = self.driver.find_element(By.XPATH, '//*[@id="menu_recruitment_viewRecruitmentModule"]/b')
         

        self.hover = ActionChains(self.driver).move_to_element(self.element).perform()
        time.sleep(3)
         
        return self

    def click_candidates(self):
        self.click_element = self.driver.find_element(By.XPATH, '//*[@id="menu_recruitment_viewCandidates"]')

        self.hover = ActionChains(self.driver).move_to_element(self.click_element).click(self.click_element).perform()
        
       
        time.sleep(3)

        return self

    def click_add(self):
        self.click_element = self.driver.find_element(By.XPATH, '//*[@id="btnAdd"]')

        self.hover = ActionChains(self.driver).move_to_element(self.click_element).click(self.click_element).perform()
        
        time.sleep(3)

        return self

    def fill_form(self):   
         self.fname = self.driver.find_element(By.XPATH, '//*[@id="addCandidate_firstName"]').send_keys("Samkelo")  
         self.mname = self.driver.find_element(By.XPATH, '//*[@id="addCandidate_middleName"]').send_keys("Sam")
         self.lname = self.driver.find_element(By.XPATH,  '//*[@id="addCandidate_lastName"]').send_keys("Samkelo")
         self.email = self.driver.find_element(By.XPATH,  '//*[@id="addCandidate_email"]' ).send_keys("samkelo@kineticskunk.com")
         self.cnumber = self.driver.find_element(By.XPATH, '//*[@id="addCandidate_contactNo"]').send_keys("780479246")

         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
         self.save_btn = Button(By.XPATH,'//*[@id="btnSave"]').click()

         time.sleep(3)
         
         return self

    def back_btn(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.back_btn = Button(By.XPATH, '//*[@id="btnBack"]').click()

        time.sleep(3)

        return self 
    def dlt_record(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click_element = self.driver.find_element(By.XPATH, '//*[@id="ohrmList_chkSelectAll"]')
        
        self.driver.implicitly_wait(15)
        self.hover = ActionChains(self.driver).move_to_element(self.click_element).click(self.click_element).perform()
        
        self.driver.find_element(By.XPATH, '//*[@id="btnDelete"]').click()
        self.driver.implicitly_wait(10)
        #self.driver.find_element(By.XPATH, '//*[@id="dialogDeleteBtn"]').click()

        time.sleep(5)

    
        return self

                


       


       