from locators.order_page_locators import OrderPageLocators
from helpers import DataCalendar


class TextAnswerDropList:
    text_how_much = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    text_want_scooters = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    text_how_rental = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    text_possible_order = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    text_extend_or_return = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    text_bringing_charges = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    text_cansel = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    text_far_life = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


class DataForOdrer:
    data_order_1 = {
        'name': 'Владислав',
        'family': 'Иванов',
        'address': 'г. Москва',
        'metro': OrderPageLocators.METRO_ROKOSOVSKI,
        'phone': '+79998887766',
        'date': DataCalendar.get_tomorrow_date(),
        'rent': OrderPageLocators.RENT_FOR_ONE_DAY,
        'color': OrderPageLocators.CHECKBOX_COLOR_BLACK,
        'comment': ''
    }

    data_order_2 = {
        'name': 'Марина',
        'family': 'Тараторкина',
        'address': 'Московская область',
        'metro': OrderPageLocators.METRO_CHERKIZOVO,
        'phone': '+799988877644',
        'date': DataCalendar.get_next_week_date(),
        'rent': OrderPageLocators.RENT_FOR_TWO_DAYS,
        'color': OrderPageLocators.CHECKBOX_COLOR_GREY,
        'comment': 'Хочу самокат'
    }


class DaraUrl:
    SCOOTER = 'https://qa-scooter.praktikum-services.ru/'
    DZEN = 'https://dzen.ru/'
