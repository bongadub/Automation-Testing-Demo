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

from behave import given, when, then

from android_behave.pageobjects.menu import MenuPageObject
from android_behave.pageobjects.scroll import  ScrollPageObject

@given('the app menu is open')
def step_impl(context):
    context.current_page = ScrollPageObject()

@when('the user click views')
def step_impl(context):
	context.current_page = ScrollPageObject()
	context.current_page.view_btn()


@when('click tabs')
def step_impl(context):
	context.current_page = MenuPageObject()
	context.current_page.open_option('Tabs')

@when('click Scrollable')
def step_impl(context):
	context.current_page = ScrollPageObject()
	context.current_page.scroll_btn()

@then('click tab 24')
def step_impl(context):
	context.current_page = ScrollPageObject()
	context.current_page.scroll_right()


