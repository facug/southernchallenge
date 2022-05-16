from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@given(u'i launch chrome browser')
def launchChromeBrowser(context):
    context.driver = webdriver.Chrome(executable_path="D:\\repos\\drivers\\chromedriver.exe")


@when(u'i open DuckGogo homepage')
def openDuckGoGo(context):
    context.driver.get("https://duckduckgo.com/")

@when('search for "{text}"')
def searchForText(context, text):
    searchInput = context.driver.find_element_by_id('search_form_input_homepage')
    searchInput.send_keys(text)
    searchInput.send_keys(Keys.ENTER)
    context.driver.implicitly_wait(10)


@then(u'verify DuckGoGo page')
def verifyDuckGoGo(context):
    status = context.driver.find_element_by_id('search_form_input').is_displayed()
    assert status is True
