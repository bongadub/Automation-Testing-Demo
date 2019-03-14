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


class ScrollPageObject(PageObject):
  def view_btn(self):
    self.view = self.driver.find_element(By.XPATH, '//*[@text="Views"]').click()
    time.sleep(3)

  def scroll_btn(self):
    self.scroll = self.driver.find_element(By.XPATH, '//*[@text="5. Scrollable"]').click()
    time.sleep(3)

  def scroll_right(self):
    self.scroll = self.driver.find_element(By.XPATH, '//*[@text="TAB 2"]').click()
    time.sleep(3)

  def view_btn(self):
       self.view = self.driver.find_element(By.XPATH, '//*[@text="Views"]').click()
       time.sleep(3)
