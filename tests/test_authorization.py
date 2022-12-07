from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_authorization_user_with_button_sign_in_authorization_user():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/section[2]/div/button').click()
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(
        'france@gmail.com')
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(
        'ceSru0-fedzat-bysbez')
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/button').click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/*[@id="root"]/div'
                                                                                                '/main/section['
                                                                                                '2]/div/button')))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()


def test_authorization_user_with_button_personal_account_authorization_user():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, './/*[@id="root"]/div/header/nav/a/p').click()
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(
        'france@gmail.com')
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(
        'ceSru0-fedzat-bysbez')
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/button').click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/*[@id="root"]/div'
                                                                                                '/main/section['
                                                                                                '2]/div/button')))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()


def test_authorization_user_with_button_in_registration_form_authorization_user():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/div/p/a').click()
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(
        'france@gmail.com')
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(
        'ceSru0-fedzat-bysbez')
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/button').click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/*[@id="root"]/div'
                                                                                                '/main/section['
                                                                                                '2]/div/button')))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()


def test_authorization_user_with_button_in_password_recovery_form_authorization_user():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/div/p/a').click()
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(
        'france@gmail.com')
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(
        'ceSru0-fedzat-bysbez')
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/button').click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/*[@id="root"]/div'
                                                                                                '/main/section['
                                                                                                '2]/div/button')))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()
