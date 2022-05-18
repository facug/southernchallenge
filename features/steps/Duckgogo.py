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


@then('verify Michael Jordan profile picture is displayed')
def verifyMichaelJordanImg(context):
    status = context.driver.find_element_by_css_selector('.module__image img[src="/i/c0e400e4.jpg"]').is_displayed()
    assert status is True


@then('verify there is one "{text}" page result')
def verifyWikipediaPageResult(context, text):
    links = context.driver.find_elements_by_css_selector('.results a[href]')
    status = False
    for link in links:
        if text in link.get_attribute("href"):
            status = False
    assert status is True



@then(u'verify DuckGoGo page')
def verifyDuckGoGo(context):
    status = context.driver.find_element_by_id('search_form_input').is_displayed()
    assert status is True
