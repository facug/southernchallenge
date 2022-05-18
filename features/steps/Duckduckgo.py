from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


@given(u'i launch chrome browser')
def launch_chrome_browser(context):
    context.driver = webdriver.Chrome(executable_path="D:\\repos\\drivers\\chromedriver.exe")


@when(u'i open DuckGogo homepage')
def open_duckduckgo_page(context):
    context.driver.get("https://duckduckgo.com/")


@when(u'i open DuckGogo theme page')
def open_duckduckgo_theme_settings_page(context):
    context.driver.get("https://duckduckgo.com/settings#theme")
    context.driver.implicitly_wait(10)


@when(u'i open DuckGogo general settings page')
def open_duckduckgo_general_settings_page(context):
    context.driver.get("https://duckduckgo.com/settings#general")


@when('search for "{text}"')
def search_for_text(context, text):
    searchInput = context.driver.find_element_by_id('search_form_input_homepage')
    searchInput.send_keys(text)
    searchInput.send_keys(Keys.ENTER)


@then('verify Michael Jordan profile picture is displayed')
def verify_michael_jordan_img(context):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[src="/i/c0e400e4.jpg"]')))
    status = context.driver.find_element_by_css_selector('img[src="/i/c0e400e4.jpg"]').is_displayed()
    assert status is True


@then('verify there is one "{text}" page result')
def verify_wikipedia_page_result(context, text):
    links = context.driver.find_elements_by_css_selector('.results a[href]')
    status = False
    for link in links:
        if text in link.get_attribute("href"):
            status = True
    assert status is True


@when(u'i change the theme to "Terminal"')
def change_theme(context):
    context.driver.find_element_by_css_selector('.set-theme[data-theme-id="t"]').click()
    context.driver.find_element_by_css_selector('.set-main-footer a').click()


@then(u'verify the background color changed')
def verify_background_color(context):
    bodyElement = context.driver.find_element_by_css_selector('.set-theme[data-theme-id="t"]')
    background_value = bodyElement.value_of_css_property('background-color')
    assert (background_value ==  "#222")


@when(u'i change the language to "{text}"')
def step_impl(context, text):
    select = Select(context.driver.find_element_by_id('setting_kad'))
    select.select_by_visible_text(text)
    context.driver.implicitly_wait(1000)


@then(u'verify the language changed to "{text}"')
def step_impl(context, text):
    select_text = Select(context.driver.find_element_by_id('setting_kad')).first_selected_option.text
    assert (select_text == text)
