from selenium.webdriver.common.by import By

class MainPageLocators:
    # Маленькая кнопка "Заказать" в header
    ORDER_MIN_BUTTON = [By.XPATH, ".//div[@class = 'Header_Nav__AGCXC']/button[text() = 'Заказать']"]
    # Большая кнопка "Заказать" (можно заменить на класс) - 'Button_UltraBig__UU3Lp'
    ORDER_BIG_BUTTON = [By.XPATH, ".//div[@class = 'Home_FinishButton__1_cWm']/button[text() = 'Заказать']"]
    # Вопросы выпадающего списка "Вопросы о главном"
    HOW_MUCH_DROP_LIST = [By.XPATH, ".//div[contains(text(), 'Сколько это стоит?')]"]  # вопрос "Сколько это стоит? И как оплатить?"
    WANT_SCOOTERS_DROP_LIST = [By.XPATH, ".//div[contains(text(), 'Хочу сразу несколько')]"]  # вопрос "Хочу сразу несколько самокатов! Так можно?"
    HOW_RENTAL_DROP_LIST = [By.XPATH, ".//div[contains(text(), 'Как рассчитывается')]"]  # вопрос "Как рассчитывается время аренды?"
    POSSIBLE_ORDER_DROP_LIST = [By.XPATH, ".//div[contains(text(), 'Можно ли заказать')]"]  # вопрос "Можно ли заказать самокат прямо на сегодня?"
    EXTEND_OR_RETURN_DROP_LIST = [By.XPATH, ".//div[contains(text(), 'Можно ли продлить')]"]  # вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
    BRINGING_CHARGES_DROP_LIST = [By.XPATH, ".//div[contains(text(), 'Вы привозите')]"]  # вопрос "Вы привозите зарядку вместе с самокатом?"
    CANCEL_DROP_LIST = [By.XPATH, ".//div[contains(text(), 'Можно ли отменить')]"]  # вопрос "Можно ли отменить заказ?"
    FAR_LIFE_DROP_LIST = [By.XPATH, ".//div[contains(text(), 'МКАД')]"]  # вопрос "Я живу за МКАДом, привезёте?"
    # Заголовок "Важные вопросы"
    IMPORTANT_QUESTIONS_HEAD = [By.XPATH, ".//div[text() = 'Вопросы о важном']"]
    # Текст в выпадающих списках
    HOW_MUCH_TEXT = [By.XPATH, ".//div[@id = 'accordion__panel-0']/p"]  # ответ 1
    WANT_SCOOTERS_TEXT = [By.XPATH, ".//div[@id = 'accordion__panel-1']/p"]  # ответ 2
    HOW_RENTAL_TEXT = [By.XPATH, ".//div[@id = 'accordion__panel-2']/p"]  # ответ 3
    POSSIBLE_ORDER_TEXT = [By.XPATH, ".//div[@id = 'accordion__panel-3']/p"]  # ответ 4
    EXTEND_OR_RETURN_TEXT = [By.XPATH, ".//div[@id = 'accordion__panel-4']/p"]  # ответ 5
    BRINGING_CHARGES_TEXT = [By.XPATH, ".//div[@id = 'accordion__panel-5']/p"]  # ответ 6
    CANCEL_TEXT = [By.XPATH, ".//div[@id = 'accordion__panel-6']/p"]  # ответ 7
    FAR_LIFE_TEXT = [By.XPATH, ".//div[@id = 'accordion__panel-7']/p"]  # ответ 8
