from selenium.webdriver.common.by import By


class BasePageLocators:
    # Маленькая кнопка "Заказать" в header
    ORDER_MIN_BUTTON = [By.XPATH, ".//div[@class = 'Header_Nav__AGCXC']/button[text() = 'Заказать']"]

    # заголовок "Самокат"
    BUTTON_HEAD_SCOOTER = [By.XPATH, ".//a[@class = 'Header_LogoScooter__3lsAR']"]

    # заголовок "Яндекс"
    BUTTON_HEAD_YANDEX = [By.XPATH, ".//a[@class = 'Header_LogoYandex__3TSOI']"]