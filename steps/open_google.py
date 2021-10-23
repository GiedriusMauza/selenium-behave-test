from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from settings.config import settings
from allocator.driver import driver
from behave import given, when, then, step


@given(u'I open google')
def step_impl(context):
    try:
        driver.navigate(settings.url)
    except:
        LogoutPage().logout()


@step(u'I enter search query')
def step_impl(context):
    print("hello")


@then("I see suggestions")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("hello2")