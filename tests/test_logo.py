import allure
from page_object.main_page import MainPage

class TestNavigitationLogo:
    @allure.title("Проверка навигации с помощью кнопки логотипа 'Самоката'")
    def test_click_on_logo_scooter(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/order")
        main_page = MainPage(driver)
        main_page.click_on_logo_scooter()
        main_page.checking_tabs()

        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/", 'Навигация на главную страницу «Самоката».'

    @allure.title("Проверка навигации с помощью кнопки логотипа 'Яндекса'")
    def test_click_on_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_logo_yandex()
        main_page.checking_tabs()
        assert driver.current_url == "https://dzen.ru/?yredirect=true", 'В новом окне должна открыться главная страница Яндекса(Дзен).'
