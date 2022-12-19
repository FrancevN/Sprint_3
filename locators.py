from selenium.webdriver.common.by import By


class Locators:
    menu_rolls = (By.XPATH, './/*[@id="root"]/div/main/section[1]/div[1]/div[1]/span')  # Кнопка "Булки"
    login = (By.NAME, 'name')  # Поле ввода имени и email в форме регистрации/входа
    password = (By.NAME, 'Пароль')  # Поле ввода пароля в форме регистрации/входа
    registration_button = (By.CLASS_NAME, 'button_button__33qZ0')  # Кнопка регистрации в форме регистрации
    registration_incorrect_password = (By.CLASS_NAME, 'input__error')  # Надпись о неверно введенном пароле
    login_forgot_password = (By.LINK_TEXT, 'Восстановить пароль')  # Кнопка восстановления пароля в форме логина
    button_sign_in = (By.CLASS_NAME, 'button_button__33qZ0')  # Кнопка "Войти в аккаунт" на главной странице/
    # Кнопка "Войти" в форме входа
    button_tab = (By.CLASS_NAME, 'tab_tab__1SPyG')  # Таб конструктора
    header_button = (By.CLASS_NAME, 'AppHeader_header__link__3D_hX')  # Кнопки в шапке
    button_sign_in_in_registration_form = (By.LINK_TEXT, 'Войти')  # Войти в форме регистрации/форме забытого пароля
    info_in_personal_account = (By.CLASS_NAME, 'Account_text__fZAIn')  # Блок информации
    # "В этом разделе вы можете изменить свои персональные данные" из личного кабинета
    header_logo = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')  # Лого в шапке
    logout = (By.CLASS_NAME, 'Account_button__14Yp3')  # Кнопка "Выйти" в личном кабинете
