from locators.main_page_locators import MainPageLocators
import allure
from pages.base_page import BasePageScooter


class MainPageScooter(BasePageScooter):

    # выпадающий список
    def open_drop_list(self, question):
        self.driver.find_element(*question).click()

    # сравнение текста
    def text_comparison_drop_list(self, answer):
        return self.driver.find_element(*answer).text

    # нажатие на большую кнопку "Заказать"
    def click_big_button_order(self):
        self.driver.find_element(*MainPageLocators.ORDER_BIG_BUTTON).click()

    # ШАГИ ДЛЯ СОКРАЩЕНИЯ ТЕСТОВ
    # ШАГ для тестирования при нажатии на вопрос
    @allure.step('Нажимаем на вопрос в разделе "Вопросы о важном"')
    def expanding_list(self, question, answer):
        self.scroll_element(MainPageLocators.IMPORTANT_QUESTIONS_HEAD)
        self.wait_and_clickable(question)
        self.open_drop_list(question)
        self.wait_and_find_element(answer)
        return self.text_comparison_drop_list(answer)

    # ШАГ нажатие на большую кнопку "Заказать"
    @allure.step('Скроллим, и нажимаем на большую кнопку "Заказать"')
    def button_order_in_page(self):
        self.scroll_element(MainPageLocators.ORDER_BIG_BUTTON)
        self.wait_and_find_element(MainPageLocators.ORDER_BIG_BUTTON)
        self.click_big_button_order()
