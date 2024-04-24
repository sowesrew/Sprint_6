from locators.order_page_locators import OrderPageLocators
import allure
from pages.base_page import BasePageScooter


class OrderPageScooter(BasePageScooter):

    # Ввод в поле "Имя"
    def enter_in_field_name(self, name):
        self.driver.find_element(*OrderPageLocators.INPUT_NAME).send_keys(name)

    # Ввод в поле "Фамилия"
    def enter_in_field_family(self, family):
        self.driver.find_element(*OrderPageLocators.INPUT_FAMILY).send_keys(family)

    # Ввод в поле "Адрес"
    def enter_in_field_address(self, address):
        self.driver.find_element(*OrderPageLocators.INPUT_ADDRESS).send_keys(address)

    # Ввод в инпут-выпадашку "Метро"
    def enter_in_field_metro(self, metro):
        self.driver.find_element(*OrderPageLocators.INPUT_DROP_METRO).click()
        self.driver.find_element(*metro).click()

    # Ввод номера телефона
    def enter_in_field_phone(self, phone):
        self.driver.find_element(*OrderPageLocators.INPUT_PHONE).send_keys(phone)

    # Нажатие на кнопку "Далее"
    def click_button_next(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_NEXT_ORDER).click()

    # Ввод даты
    def enter_in_field_calendar(self, date):
        self.driver.find_element(*OrderPageLocators.INPUT_WHEN_BRING_ORDER).send_keys(date)
        self.driver.find_element(*OrderPageLocators.SELECTED_DAY_CALENDAR).click()

    # Ввод "Срок аренды"
    def enter_in_rental_period(self, rent):
        self.driver.find_element(*OrderPageLocators.INPUT_DROP_RENTAL_PERIOD).click()
        self.driver.find_element(*rent).click()

    # Клик по цвету
    def click_checkbox_color(self, color):
        self.driver.find_element(*color).click()

    # Ввод комментария для курьера
    def enter_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.INPUT_COMMENT).send_keys(comment)

    # Клик по кнопке "Заказать"
    def click_order_final(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_FINAL_ORDER).click()

    # Всплывающее окно - "Заказ оформлен" - отображается кнопка "Показать статус"
    def successful_order(self):
        return self.driver.find_element(*OrderPageLocators.VIEW_STATUS_BUTTON).text

    # ШАГИ ДЛЯ СОКРАЩЕНИЯ ТЕСТОВ
    # Первый ШАГ в заполнении заказа
    @allure.step('Заполняем поля на первой странице заказа: имя, фамилию, адрес, метро, телефон, затем переходим к следующему шагу')
    def first_step_order(self, name, family, address, metro, phone):
        self.enter_in_field_name(name)
        self.enter_in_field_family(family)
        self.enter_in_field_address(address)
        self.enter_in_field_metro(metro)
        self.enter_in_field_phone(phone)
        self.click_button_next()
        self.wait_and_find_element(OrderPageLocators.BUTTON_FINAL_ORDER)

    # Второй ШАГ в заполнении заказа
    @allure.step('Заполняем поля на второй странице заказа: дату, период, цвет, комментарий и нажимаем "Заказать"')
    def second_step_order(self, date, rent, color, comment):
        self.enter_in_field_calendar(date)
        self.enter_in_rental_period(rent)
        self.click_checkbox_color(color)
        self.enter_comment(comment)
        self.click_order_final()

    # ШАГ подтверждение заказа
    @allure.step('Нажимаем кнопку "Да" в окне подтверждения заказа')
    def click_order_confirmation(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_YES).click()
