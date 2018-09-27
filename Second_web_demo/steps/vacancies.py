from behave import given, when, then

from pageobjects.vacancies import VacanciesPageObject

@given('the log in page is open')
def step_impl(context):
	context.current_page = VacanciesPageObject()
	context.current_page.open()


@when('the user logs in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
	user = {'username': username, 'password': password}
	context.current_page = context.current_page.login(user)	

@then('the user hovers over Recruitment tab')
def step_impl(context):
	context.current_page = VacanciesPageObject()
	context.current_page.hover()

@given('the user clicks on vacancies')
def step_impl(context):
	context.current_page = VacanciesPageObject()
	context.current_page.click_vacancies()	

