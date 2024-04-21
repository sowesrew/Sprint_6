from pages.main_page import MainPageScooter
from pages.order_page import OrderPageScooter
from locators.order_page_locators import OrderPageLocators
from conftest import driver
from helpers import DataCalendar
import allure


class TestOrderScooter:

    @allure.title('Проверка заказа через кнопку "Заказать" в хэдере')
    @allure.description('Позитивный сценарий создания заказа аренды самоката')
    def test_order_button_in_header(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')

        seach_button_order = MainPageScooter(driver)
        test_order_scooter = OrderPageScooter(driver)

        seach_button_order.click_button_order_in_header()

        test_order_scooter.first_step_order('Владислав', 'Иванов', 'г. Москва', OrderPageLocators.METRO_ROKOSOVSKI, '+79998887766')
        test_order_scooter.second_step_order(DataCalendar.get_tomorrow_date(), OrderPageLocators.RENT_FOR_ONE_DAY, OrderPageLocators.CHECKBOX_COLOR_BLACK, '')
        test_order_scooter.click_order_confirmation()

        head_succesful_order = test_order_scooter.successful_order()
        assert head_succesful_order == 'Посмотреть статус'

    @allure.title('Проверка заказа через большую кнопку "Заказать" на сайте')
    @allure.description('Позитивный сценарий создания заказа аренды самоката')
    def test_order_big_button(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')

        seach_button_order = MainPageScooter(driver)
        test_order_scooter = OrderPageScooter(driver)

        seach_button_order.button_order_in_page()

        test_order_scooter.first_step_order('Марина', 'Тараторкина', 'Московская область', OrderPageLocators.METRO_CHERKIZOVO, '+799988877644')
        test_order_scooter.second_step_order(DataCalendar.get_next_week_date(), OrderPageLocators.RENT_FOR_TWO_DAYS,OrderPageLocators.CHECKBOX_COLOR_GREY, 'Хочу самокат')
        test_order_scooter.click_order_confirmation()

        head_succesful_order = test_order_scooter.successful_order()
        assert head_succesful_order == 'Посмотреть статус'

    @allure.title('Проверка перехода на главную страницу')
    @allure.description('Если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')
    def test_go_to_main_page(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/order')

        test_order_scooter = OrderPageScooter(driver)

        test_order_scooter.click_header_scooter()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка перехода на страницу Дзена')
    @allure.description('Если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.')
    def test_go_to_dzen(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')

        test_order_scooter = OrderPageScooter(driver)

        test_order_scooter.click_header_yandex()
        test_order_scooter.wait_tab_open()
        driver.switch_to.window(driver.window_handles[-1])
        test_order_scooter.wait_loading_dzen()
        assert 'https://dzen.ru/' in driver.current_url
