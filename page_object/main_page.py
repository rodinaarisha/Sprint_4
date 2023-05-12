import allure
from page_object.base_page import BasePage
from page_object.locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Даем согласие на cookies")
    def accept_cookie(self):
        cookie = self.find_element(MainPageLocators.accept_cookies)
        cookie.click()
    @allure.step("Кликаем на вопрос из раздела 'Вопросы о важном'")
    def check_answers_in_questions_about_important(self, question_pos):
        self.wait_element(MainPageLocators.title_questions_about_important[1])
        self.wait_element(MainPageLocators.menu[1])
        button_accordions = self.find_elements(MainPageLocators.questions_menu)
        button_accordions[question_pos].click()
        self.wait_element(MainPageLocators.menu[1])
        self.wait_element(MainPageLocators.questions_menu[1])
        self.wait_element(MainPageLocators.menu[1])

    @allure.step("Кликаем на кнопку логотипа Самоката")
    def click_on_logo_scooter(self):
        click_on_logo = self.find_element(MainPageLocators.button_scooter)
        click_on_logo.click()

    @allure.step("Кликаем на кнопку логотипа Яндекса")
    def click_on_logo_yandex(self):
        self.find_element(MainPageLocators.button_yandex).click()

    @allure.step("Проверка вкладок")
    def checking_tabs(self):
        number_of_tabs = len(self.driver.window_handles)
        if number_of_tabs > 1:
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.wait_element(MainPageLocators.element_from_yandex[1])

    @allure.step("Кликаем кнопку 'Заказать'")
    def click_order(self, xpath_element):
        self.find_element(xpath_element).click()
