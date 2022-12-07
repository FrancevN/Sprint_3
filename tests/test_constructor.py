from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_constructor_rolls_move_to_rolls():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/section[1]/div[1]/div[3]/span').click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/*[@id="root"]/div'
                                                                                                '/main/section['
                                                                                                '1]/div[2]/h2[3]')))
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/section[1]/div[1]/div[1]/span').click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/*[@id="root"]/div'
                                                                                                '/main/section['
                                                                                                '1]/div[2]/h2[1]')))
    assert driver.find_element(By.XPATH, './/*[@id="root"]/div/main/section[1]/div[2]/h2[1]').text == \
           'Булки'
    driver.quit()


def test_constructor_sauce_move_to_sauce():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/section[1]/div[1]/div[2]/span').click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, './/*[@id="root"]/div/main/section[1]/div[2]/h2[2]')))
    assert driver.find_element(By.XPATH, './/*[@id="root"]/div/main/section[1]/div[2]/h2[2]').text == \
           'Соусы'
    driver.quit()


def test_constructor_toppings_move_to_toppings():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, './/*[@id="root"]/div/main/section[1]/div[1]/div[3]/span').click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, './/*[@id="root"]/div/main/section[1]/div[2]/h2[3]')))
    assert driver.find_element(By.XPATH, './/*[@id="root"]/div/main/section[1]/div[2]/h2[3]').text == \
           'Начинки'
    driver.quit()
