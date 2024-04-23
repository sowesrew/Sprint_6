from pages.main_page import MainPageScooter
from pages.order_page import OrderPageScooter
from conftest import driver
import allure
from data import DataForOdrer


class TestOrderScooter:

    @allure.title('Проверка заказа через кнопку "Заказать" в хэдере')
    @allure.description('Позитивный сценарий создания заказа аренды самоката')
    def test_order_button_in_header(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        seach_button_order = MainPageScooter(driver)
        test_order_scooter = OrderPageScooter(driver)
        seach_button_order.click_button_order_in_header()
        test_order_scooter.first_step_order(DataForOdrer.data_order_1['name'], DataForOdrer.data_order_1['family'], DataForOdrer.data_order_1['address'], DataForOdrer.data_order_1['metro'], DataForOdrer.data_order_1['phone'])
        test_order_scooter.second_step_order(DataForOdrer.data_order_1['date'], DataForOdrer.data_order_1['rent'], DataForOdrer.data_order_1['color'], DataForOdrer.data_order_1['comment'])
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
        test_order_scooter.first_step_order(DataForOdrer.data_order_2['name'], DataForOdrer.data_order_2['family'], DataForOdrer.data_order_2['address'], DataForOdrer.data_order_2['metro'], DataForOdrer.data_order_2['phone'])
        test_order_scooter.second_step_order(DataForOdrer.data_order_2['date'], DataForOdrer.data_order_2['rent'], DataForOdrer.data_order_2['color'], DataForOdrer.data_order_2['comment'])
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
        test_order_scooter.wait_and_open_tab()
        driver.switch_to.window(driver.window_handles[-1])
        test_order_scooter.wait_and_title_tab()
        assert 'https://dzen.ru/' in driver.current_url
