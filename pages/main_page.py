from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators


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
    def wait_text_answer(self, answer):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(answer))

    # сравнение текста
    def text_comparison_drop_list(self, answer):
        return self.driver.find_element(*answer).text

    def expanding_list(self, question, answer):
        self.scroll_drop_list()
        self.open_drop_list(question)
        self.wait_text_answer(answer)
        return self.text_comparison_drop_list(answer)
