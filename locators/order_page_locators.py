from selenium.webdriver.common.by import By


class OrderPageLocators:
    # первая "страница"
    # инпут "Имя"
    INPUT_NAME = [By.XPATH, ".//input[@placeholder = '* Имя']"]
    # инпут "Фамилия"
    INPUT_FAMILY = [By.XPATH, ".//input[@placeholder = '* Фамилия']"]
    # инпут "Адрес"
    INPUT_ADDRESS = [By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']"]
    # инпут-выпадашка "Станция метро"
    INPUT_DROP_METRO = [By.XPATH, ".//input[@placeholder = '* Станция метро']"]
    # Cтанции метро
    METRO_ROKOSOVSKI = [By.XPATH, ".//li[@data-index = 0]"]
    METRO_CHERKIZOVO = [By.XPATH, ".//li[@data-index = 1]"]
    # инпут "Телефон"
    INPUT_PHONE = [By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']"]
    # кнопка "Далее"
    BUTTON_NEXT_ORDER = [By.XPATH, ".//button[text() = 'Далее']"]

    # вторая "страница"
    # инпут-календарь "Когда привезти заказ"
    INPUT_WHEN_BRING_ORDER = [By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"]
    SELECTED_DAY_CALENDAR = [By.XPATH, ".//div[contains(@class, 'react-datepicker__day--selected')]"]
    # выпадашка "Срок аренды"
    INPUT_DROP_RENTAL_PERIOD = [By.CLASS_NAME, "Dropdown-placeholder"]
    # Сроки аренды
    RENT_FOR_ONE_DAY = [By.XPATH, ".//div[text() = 'сутки']"]
    RENT_FOR_TWO_DAYS = [By.XPATH, ".//div[text() = 'двое суток']"]
    # чек-боксы "Цвет"
    CHECKBOX_COLOR_BLACK = [By.XPATH, ".//label[@for= 'black']"]  # цвет "Чёрный жемчуг"
    CHECKBOX_COLOR_GREY = [By.XPATH, ".//label[@for= 'grey']"]  # цвет "Серая безысходность"
    # инпут "Комментарий для курьера"
    INPUT_COMMENT = [By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']"]
    # кнопка "Заказать"
    BUTTON_FINAL_ORDER = [By.XPATH, ".//div[@class = 'Order_Buttons__1xGrp']/button[text() = 'Заказать']"]

    # всплывающее окно
    # кнопка "Да"
    BUTTON_YES = [By.XPATH, ".//div[@class = 'Order_Buttons__1xGrp']/button[text() = 'Да']"]

    # кнопка "Посмотреть статус"
    VIEW_STATUS_BUTTON = [By.XPATH, ".//div[@class = 'Order_NextButton__1_rCA']/button[text() = 'Посмотреть статус']"]
