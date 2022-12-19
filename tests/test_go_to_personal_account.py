from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


def test_go_to_personal_account_open_personal_account(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*Locators.login).send_keys('france@gmail.com')
    driver.find_element(*Locators.password).send_keys('ceSru0-fedzat-bysbez')
    driver.find_element(*Locators.button_sign_in).click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.button_tab))
    driver.find_elements(*Locators.header_button)[2].click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.info_in_personal_account))
    assert driver.find_element(*Locators.info_in_personal_account).text == 'В этом разделе вы можете изменить свои ' \
                                                                           'персональные данные'
