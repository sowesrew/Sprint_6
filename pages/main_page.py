from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
import allure


class MainPageScooter:
    def __init__(self, driver):
        self.driver = driver

    # скролл до списка
    def scroll_drop_list(self):
        head_drop_list = self.driver.find_element(*MainPageLocators.IMPORTANT_QUESTIONS_HEAD)
        self.driver.execute_script("arguments[0].scrollIntoView();", head_drop_list)

    # выпадающий список
    def open_drop_list(self, question):
        self.driver.find_element(*question).click()

    # ожидание
    def wait_text_question(self, question):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(question))

    # ожидание
    def wait_text_answer(self, answer):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(answer))

    # сравнение текста
    def text_comparison_drop_list(self, answer):
        return self.driver.find_element(*answer).text

    # скролл до большой кнопки "Заказать"
    def scroll_button_order(self):
        big_button_order = self.driver.find_element(*MainPageLocators.ORDER_BIG_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", big_button_order)

    # ожидание, пока загрузится кнопка
    def wait_loading_big_button_order(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(MainPageLocators.ORDER_BIG_BUTTON))

    # нажатие на большую кнопку "Заказать"
    def click_big_button_order(self):
        self.driver.find_element(*MainPageLocators.ORDER_BIG_BUTTON).click()

    # ШАГИ ДЛЯ СОКРАЩЕНИЯ ТЕСТОВ
    # ШАГ для тестирования при нажатии на вопрос
    @allure.step('Нажимаем на вопрос в разделе "Вопросы о важном"')
    def expanding_list(self, question, answer):
        self.scroll_drop_list()
        self.wait_text_question(question)
        self.open_drop_list(question)
        self.wait_text_answer(answer)
        return self.text_comparison_drop_list(answer)

    # ШАГ нажатие на кнопку "Заказать" в хэдере
    @allure.step('Нажимаем на кнопку "Заказать" в хэдере')
    def click_button_order_in_header(self):
        self.driver.find_element(*MainPageLocators.ORDER_MIN_BUTTON).click()

    # ШАГ нажатие на большую кнопку "Заказать"
    @allure.step('Скроллим, и нажимаем на большую кнопку "Заказать"')
    def button_order_in_page(self):
        self.scroll_button_order()
        self.wait_loading_big_button_order()
        self.click_big_button_order()
