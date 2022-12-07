from selenium.webdriver.common.by import By
from selenium import webdriver


def test_registration_new_user_add_user():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Илюша')
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(
        'f@gmail.com')
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('kkkkkk')
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/button').click()

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()


def test_registration_new_user_not_correct_password_error():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Илюша')
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(
        'frfdfan@gmail.com')
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('kkk')
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/button').click()

    assert driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[3]/div/p').text == \
           'Некорректный пароль'
    driver.quit()
