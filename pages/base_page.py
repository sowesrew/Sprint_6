from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
import allure


class BasePageScooter:
    def __init__(self, driver):
        self.driver = driver

    # ждём, пока элемент прогрузится и отобразится
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # ждём пока элемент прогрузится и станет кликабельным
    def wait_and_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    # ждём пока откроется вторая вкладка
    def wait_and_open_tab(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.number_of_windows_to_be(2))

    # ждём, пока отобразится заголовок страницы Дзен
    def wait_and_title_tab(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.title_is('Дзен'))

    # скролл до нужного элемента
    def scroll_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # нажатие на кнопку "Заказать" в хэдере
    @allure.step('Нажимаем на кнопку "Заказать" в хэдере')
    def click_button_order_in_header(self):
        self.driver.find_element(*BasePageLocators.ORDER_MIN_BUTTON).click()

    # Нажатие на логотип "Самокат" в хэдере
    def click_header_scooter(self):
        self.driver.find_element(*BasePageLocators.BUTTON_HEAD_SCOOTER).click()

    # Нажатие на логотип "Яндекс" в хэдере
    def click_header_yandex(self):
        self.driver.find_element(*BasePageLocators.BUTTON_HEAD_YANDEX).click()
