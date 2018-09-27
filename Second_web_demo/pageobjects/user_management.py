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


class UserPageObject(PageObject):
    def init_page_elements(self):
        self.username = InputText(By.NAME, 'txtUsername')
        self.password = InputText(By.NAME, 'txtPassword')
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
        time.sleep(5)
        self.username.text = user['username']
        self.password.text = user['password']
        self.login_button.click()
        time.sleep(5)

    def admin_tab(self):
        self.admin = self.driver.find_element(By.XPATH, '//*[@id="menu_admin_viewAdminModule"]').click()
        time.sleep(3)
        return self

    def add_btn(self):
        self.add = Button(By.ID, 'btnAdd').click()
        time.sleep(3)

    def add_user(self):
        self.user_role = self.driver.find_element(By.XPATH, '//*[@id="systemUser_userType"]/option[@value=2]').click()
        time.sleep(2)
        self.employee_name = self.driver.find_element(By.XPATH, '//*[@id="systemUser_employeeName_empName"]').send_keys('Reeja R Rajan')
        time.sleep(2)
        self.username = self.driver.find_element(By.XPATH, '//*[@id="systemUser_userName"]').send_keys('reeja.r')
        time.sleep(2)
        self.status = self.driver.find_element(By.XPATH, '//*[@id="systemUser_status"]/option[@value=1]').click()
        time.sleep(2)
        self.password = self.driver.find_element(By.XPATH, '//*[@id="systemUser_password"]').send_keys('Passw0rd123')
        time.sleep(2)
        self.confirm_pass = self.driver.find_element(By.XPATH, '//*[@id="systemUser_confirmPassword"]').send_keys('Passw0rd123')
        time.sleep(2)
        self.save_button = Button(By.XPATH, '//*[@id="btnSave"]').click()
        time.sleep(5)

        


