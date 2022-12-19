from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


def test_move_from_personal_account_to_constructor_open_constructor(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*Locators.login).send_keys('france@gmail.com')
    driver.find_element(*Locators.password).send_keys('ceSru0-fedzat-bysbez')
    driver.find_element(*Locators.button_sign_in).click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.button_tab))
    driver.find_elements(*Locators.header_button)[2].click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.info_in_personal_account))
    driver.find_element(*Locators.header_button).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_move_from_personal_account_to_logo_open_constructor(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*Locators.login).send_keys('france@gmail.com')
    driver.find_element(*Locators.password).send_keys('ceSru0-fedzat-bysbez')
    driver.find_element(*Locators.button_sign_in).click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.button_tab))
    driver.find_elements(*Locators.header_button)[2].click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.info_in_personal_account))
    driver.find_element(*Locators.header_logo).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
