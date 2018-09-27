from behave import given, when, then

from pageobjects.candidates import CandidatesPageObject


@given('the user clicks on candidates')
def step_impl(context):
	context.current_page = CandidatesPageObject()
	context.current_page.click_candidates()	

@when('the user clicks on add button')
def step_impl(context):
	context.current_page = CandidatesPageObject()
	context.current_page.click_add()

@then('the user fills the candidates web form')
def step_impl(context):
	context.current_page = CandidatesPageObject()
	context.current_page.fill_form()	

@when('the user views the candidate information and clicks the back button')	
def step_imol(context):
	context.current_page = CandidatesPageObject()
	context.current_page.back_btn()

@given('the user deletes the candidates records')
def step_impl(context):
	context.current_page = CandidatesPageObject()
	context.current_page.dlt_record()	

@when('the user clicks the checklist button')	
def step_impl(context):
	context.current_page = CandidatesPageObject()
	context.current_page.dlt_record()

@then('the user clicks the delete button')
def step_impl(context):
	context.current_page = CandidatesPageObject()		
	context.current_page.dlt_record()
