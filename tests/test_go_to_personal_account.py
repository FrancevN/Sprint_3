from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_go_to_personal_account_open_personal_account():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(
        'france@gmail.com')
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(
        'ceSru0-fedzat-bysbez')
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/form/button').click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/*[@id="root"]/div'
                                                                                                '/main/section['
                                                                                                '2]/div/button')))
    driver.find_element(By.XPATH, './/*[@id="root"]/div/header/nav/a/p').click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/*[@id="root"]/div'
                                                                                                '/main/div/nav/p')))
    assert driver.find_element(By.XPATH, './/*[@id="root"]/div/main/div/nav/p').text == \
           'В этом разделе вы можете изменить свои персональные данные'
