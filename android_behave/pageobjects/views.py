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
import time
from selenium.webdriver.common.by import By


from appium.webdriver.common.mobileby import MobileBy

from toolium.pageobjects.page_object import PageObject

from random import randint

from android_behave.pageobjects.synchronization import Synchronization

from appium.webdriver.common.touch_action import TouchAction

from toolium.pageobjects.page_object import PageObject
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
from toolium.pageelements import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import selenium.webdriver.support.expected_conditions as WAITCON
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from toolium.pageelements import InputText, Button
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.command import Command

from actions import action, Action, Actions

import random
import string
import time

import inspect



class ViewsPageObject(PageObject):
	def view_btn(self):
		try:
		    self.view = self.driver.find_element(By.XPATH, '//*[@text="Views"]').click()
		    time.sleep(3)

		    return True
		except NoSuchElementException:
		    self.auto_log("error", "Element {} does not exist".format(element))
		    return None    

	def animation_btn(self):
		try:
		    self.animation = self.driver.find_element(By.XPATH, '//*[@text="Animation"]').click()
		    time.sleep(3)

		    return True
		except NoSuchElementException:
		    self.auto_log("error", "Element {} does not exist".format(element))
		    return None    

	def trans_btn(self):
		try:
			self.transition = self.driver.find_element(By.XPATH, '//*[@text="3D Transition"]').click()
			time.sleep(3)

			return True
		except NoSuchElementException:
			self.auto_log("error", "Element {} does not exist".format(element))
			return None

	def lyon_btn(self):
		try:
			self.lyon = self.driver.find_element(By.XPATH, '//*[@text="Lyon"]').click()
			time.sleep(3)

			return True
		except NoSuchElementException:
			self.auto_log("error", "Element {} does not exist".format(element))
			return None