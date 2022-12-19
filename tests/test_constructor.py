from locators import Locators


def test_constructor_rolls_move_to_rolls(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_elements(*Locators.button_tab)[2].click()
    driver.find_element(*Locators.button_tab).click()
    x = driver.find_elements(*Locators.button_tab)
    assert 'tab_tab_type_current' in x[0].get_attribute("class")


def test_constructor_sauce_move_to_sauce(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_elements(*Locators.button_tab)[1].click()
    x = driver.find_elements(*Locators.button_tab)
    assert 'tab_tab_type_current' in x[1].get_attribute("class")


def test_constructor_toppings_move_to_toppings(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_elements(*Locators.button_tab)[2].click()
    x = driver.find_elements(*Locators.button_tab)
    assert 'tab_tab_type_current' in x[2].get_attribute("class")
