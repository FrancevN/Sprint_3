from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


def test_authorization_user_with_button_sign_in_authorization_user(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*Locators.button_sign_in).click()
    driver.find_element(*Locators.login).send_keys('france@gmail.com')
    driver.find_element(*Locators.password).send_keys('ceSru0-fedzat-bysbez')
    driver.find_element(*Locators.button_sign_in).click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.button_tab))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_authorization_user_with_button_personal_account_authorization_user(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_elements(*Locators.header_button)[2].click()
    driver.find_element(*Locators.login).send_keys('france@gmail.com')
    driver.find_element(*Locators.password).send_keys('ceSru0-fedzat-bysbez')
    driver.find_element(*Locators.button_sign_in).click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.button_tab))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_authorization_user_with_button_in_registration_form_authorization_user(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*Locators.button_sign_in_in_registration_form).click()
    driver.find_element(*Locators.login).send_keys('france@gmail.com')
    driver.find_element(*Locators.password).send_keys('ceSru0-fedzat-bysbez')
    driver.find_element(*Locators.button_sign_in).click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.button_tab))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_authorization_user_with_button_in_password_recovery_form_authorization_user(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(*Locators.button_sign_in_in_registration_form).click()
    driver.find_element(*Locators.login).send_keys('france@gmail.com')
    driver.find_element(*Locators.password).send_keys('ceSru0-fedzat-bysbez')
    driver.find_element(*Locators.button_sign_in).click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.button_tab))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
