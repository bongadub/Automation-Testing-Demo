# -*- coding: utf-8 -*-
u"""
Copyright 2015 Telefónica Investigación y Desarrollo, S.A.U.
This file is part of Toolium.
<<<<<<< HEAD
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
=======

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

>>>>>>> master
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import time
from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class MessagingPageObject(PageObject):
	def os_btn(self):
		self.os_optioon = self.driver.find_element(By.XPATH, '//*[@text="OS"]').click()
		time.sleep(2)

	def sms_btn(self):
		self.sms_option = self.driver.find_element(By.XPATH, '//*[@text="SMS Messaging"]').click()
		time.sleep(2)

	def msg_details(self):
		self.recipient_lbl = self.driver.find_elements(By.XPATH, '//*/android.widget.EditText')[0].send_keys('0614206270')
		self.msg_lbl = self.driver.find_elements(By.XPATH, '//*/android.widget.EditText')[1].send_keys('Hello there! This an automated text, please feel free not to reply . Team (KS)')
		#updated the click button to be able to click both on emulator and real device
		self.button = self.driver.find_elements(By.XPATH, '//*/android.widget.Button')[0].click()
		time.sleep(3)
