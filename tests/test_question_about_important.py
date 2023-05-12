import pytest
import allure
from page_object.locators import MainPageLocators
from page_object.main_page import MainPage
from page_object.main_page import BasePage
from data import DataExample


class TestQuestion:

    @pytest.mark.parametrize('question_index', [i for i in range(8)])
    @allure.title("Проверка выпадающего списка в разделе «Вопросы о важном")
    def test_click_on_question_and_check_answer(self, driver, question_index):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        main_page.accept_cookie()
        base_page.scroll_down()
        main_page.check_answers_in_questions_about_important(question_index)
        actual_result = base_page.find_elements(MainPageLocators.answers_menu)[question_index].text
        expected_result = DataExample.dictionary_question_and_answers[base_page.find_elements(MainPageLocators.questions_menu)[question_index].text]
        assert actual_result == expected_result, 'Ответ на вопрос не совпадает со значением в словаре'
