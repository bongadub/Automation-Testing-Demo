# -*- coding: utf-8 -*-
u"""
Copyright 2015 Telefónica Investigación y Desarrollo, S.A.U.
This file is part of Toolium.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

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


class AssignLeavePageObject(PageObject):
    def init_page_elements(self):
        self.username = InputText(By.XPATH, '//*[@id="txtUsername"]')
        self.password = InputText(By.XPATH, '//*[@id="txtPassword"]')
        self.login_button = Button(By.XPATH, '//*[@id="btnLogin"]')

    def open(self):
        """ Open login url in browser

        :returns: this page object instance
        """
        self.driver.get('{}/login'.format(self.config.get('Test', 'url')))
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
        self.logger.debug("Login with user '%s'", user['username'])
        self.username.text = user['username']
        self.password.text = user['password']
        self.login_button.click()
        time.sleep(5)

    def assign_leave(self):
        self.assign_leave_btn = self.driver.find_element(By.XPATH, '//*[@id="dashboard-quick-launch-panel-menu_holder"]/table/tbody/tr/td[1]/div/a').click()
        time.sleep(3)
        return self

    def leave_details(self):
        self.empl_name = self.driver.find_element(By.XPATH, '//*[@id="assignleave_txtEmployee_empName"]').send_keys('J')
        time.sleep(2)
        self.list = self.driver.find_element(By.XPATH, '/html/body/div[6]/ul/li[1]').click()
        time.sleep(2)
        self.leave_type = self.driver.find_element(By.XPATH, '//*[@id="assignleave_txtLeaveType"]/option[@value=1]').click()
        time.sleep(2)
        self.from_date = self.driver.find_element(By.XPATH, '//*[@id="assignleave_txtFromDate"]').click()
        time.sleep(2)
        self.start_date = self.driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[4]/a').click()
        time.sleep(2)
        self.to_date = self.driver.find_element(By.XPATH, '//*[@id="assignleave_txtToDate"]').click()
        time.sleep(5)
        self.end_date = self.driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[5]/a').click()
        time.sleep(5)
        self.button = Button(By.XPATH, '//*[@id="assignBtn"]').click()
        time.sleep(5)

    def ok_btn(self):
        self.OK_button = Button(By.XPATH, '//*[@id="confirmOkButton"]').click()
        time.sleep(5)
        return self
        
