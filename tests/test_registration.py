from uuid import uuid4
from locators import Locators


def test_registration_new_user_add_user(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*Locators.login).send_keys('Messi')
    driver.find_elements(*Locators.login)[1].send_keys(str(uuid4()) + '@gmail.com')
    driver.find_element(*Locators.password).send_keys(str(uuid4()))
    driver.find_element(*Locators.registration_button).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


def test_registration_new_user_not_correct_password_error(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*Locators.login).send_keys('Messi')
    driver.find_elements(*Locators.login)[1].send_keys(str(uuid4()) + '@gmail.com')
    driver.find_element(*Locators.password).send_keys('kkk')
    driver.find_element(*Locators.registration_button).click()
    assert driver.find_element(*Locators.registration_incorrect_password).text == 'Некорректный пароль'
