import pytest
import allure
from page_object.locators import MainPageLocators
from page_object.main_page import MainPage
from page_object.order_page import OrderPageFillingData
from page_object.order_page import RentPageFillingData


class TestPositiveOrder:

    @pytest.mark.parametrize('enter_button, station, name, last_name, address_to_take, '
                             'phone_number, date, index, color_index, message',
                             [pytest.param(MainPageLocators.button_order_up,
                                           "Сокол", "Арина", "Родина",
                                           "Москва, ул Ленинградский проспект, 71а ст4 кв12", "89378761223",
                                           "20.05.2023", 3, 1, "Домофон не работает, необходимо будет позвонить перед подъездом"),

                              pytest.param(MainPageLocators.button_order_down,
                                           "Митино", "Анна", "Андреева",
                                           "Москва, ул Митинская, 27 кв 27", "+78765676543",
                                           "18.10.2023", 4, 0, "Привозите после 18:00")])
    @allure.title("Проверка оформления заказа")
    def test_order(self, driver, enter_button, station, name, last_name,
                   address_to_take, phone_number, date, index, color_index, message):
        main_page = MainPage(driver)
        order_page = OrderPageFillingData(driver)
        rent_page = RentPageFillingData(driver)
        main_page.accept_cookie()
        main_page.click_order(enter_button)

        order_page.filling_order_data(
                                     name=name,
                                     last_name=last_name,
                                     address_to_take=address_to_take,
                                     station=station,
                                     phone_number=phone_number)

        order_page.click_next()

        rent_page.filling_about_rent_date(
                                              date=date,
                                              index=index,
                                              color=color_index,
                                              message=message)

        rent_page.click_on_button_to_order()
        rent_page.click_yes_on_modal_menu()

        assert "Заказ оформлен" in rent_page.completed_order(), 'Всплывающее окно с сообщением об успешном создании заказа должно отображаться.'
