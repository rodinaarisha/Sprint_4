import allure
from selenium.webdriver import Keys
from page_object.base_page import BasePage
from page_object.locators import OrderPageLocators


class OrderPageFillingData(BasePage):
    @allure.step("Ввод Имени")
    def set_name(self, name):
        self.find_element(OrderPageLocators.field_name).clear()
        self.find_element(OrderPageLocators.field_name).send_keys(name)

    @allure.step("Ввод Фамилим")
    def set_last_name(self, last_name):
        self.find_element(OrderPageLocators.field_last_name).clear()
        self.find_element(OrderPageLocators.field_last_name).send_keys(last_name)

    @allure.step("Ввод адреса")
    def set_address(self, address):
        self.find_element(OrderPageLocators.field_address).clear()
        self.find_element(OrderPageLocators.field_address).send_keys(address)

    @allure.step("Ввод номера телефона")
    def set_phone_number(self, phone_number):
        self.find_element(OrderPageLocators.field_phone_number).clear()
        self.find_element(OrderPageLocators.field_phone_number).send_keys(phone_number)

    @allure.step("Выбор остановки метро")
    def set_metro_station(self, station):
        self.find_element(OrderPageLocators.field_subway_station).click()
        self.find_element(OrderPageLocators.field_subway_station).send_keys(station)
        self.find_element(OrderPageLocators.field_subway_station).send_keys(Keys.ARROW_DOWN + Keys.ENTER)

    @allure.step("Клик на кнопку продолжить")
    def click_next(self):
        self.find_element(OrderPageLocators.button_next).click()

    @allure.step("Заполнение формы 'Для кого самокат'")
    def filling_order_data(self, name, last_name, address_to_take, station, phone_number):
        self.wait_element(OrderPageLocators.field_name[1])
        self.wait_element(OrderPageLocators.field_last_name[1])
        self.wait_element(OrderPageLocators.field_address[1])
        self.wait_element(OrderPageLocators.field_subway_station[1])
        self.wait_element(OrderPageLocators.field_phone_number[1])
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address_to_take)
        self.set_metro_station(station)
        self.set_phone_number(phone_number)


class RentPageFillingData(BasePage):
    @allure.step("Ввод даты доставки")
    def set_when_to_bring(self, date):
        self.find_element(OrderPageLocators.field_when_to_bring).send_keys(date)

    @allure.step("Выбор срока аренды")
    def set_rental_period(self, index):
        self.find_element(OrderPageLocators.field_rental_period).click()
        self.find_elements(OrderPageLocators.rental_period_menu)[index].click()

    @allure.step("Выбор цвета самоката")
    def set_scooter_color(self, color_index):
        self.find_elements(OrderPageLocators.field_scooter_color)[color_index].click()

    @allure.step("Заполнение комментария для курьера")
    def set_comment_for_the_courier(self, message):
        self.find_element(OrderPageLocators.field_comment).send_keys(message)

    @allure.step("Заполнение формы Про аренду")
    def filling_about_rent_date(self, date, index, color, message):
        self.wait_element(OrderPageLocators.field_comment[1])

        self.set_when_to_bring(date)
        self.set_rental_period(index)
        self.set_scooter_color(color)
        self.set_comment_for_the_courier(message)

    @allure.step("Клик на  кнопку 'Заказать'")
    def click_on_button_to_order(self):
        self.find_element(OrderPageLocators.button_to_order).click()

    @allure.step("Клик на кнопку 'Да'")
    def click_yes_on_modal_menu(self):
        self.find_elements(OrderPageLocators.yes_or_no_buttons)[1].click()

    @allure.step("Получение информации об оформленном заказе")
    def completed_order(self):
        text = self.find_element(OrderPageLocators.info_about_order).text
        return text
