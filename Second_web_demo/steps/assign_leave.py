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

from pageobjects.assign_leave import AssignLeavePageObject


@given('the home page is open')
def step_impl(context):
    context.current_page = AssignLeavePageObject()
    context.current_page.open()


@when('the admin logs in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    user = {'username': username, 'password': password}
    context.current_page = context.current_page.login(user)

@when('the admin clicks Assign Leave')
def step_impl(context):
	context.current_page = AssignLeavePageObject()
	context.current_page.assign_leave()

@when('the admin enters leave details')
def step_impl(context):
	context.current_page = AssignLeavePageObject()
	context.current_page.leave_details()

@then('the admin clicks OK button')
def step_impl(context):
	context.current_page = AssignLeavePageObject()
	context.current_page.ok_btn()