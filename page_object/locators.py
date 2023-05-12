from selenium.webdriver.common.by import By


class MainPageLocators:

    title_questions_about_important = [By.XPATH, ".//div[text()='Вопросы о важном']"]  # Заголовок Вопросы о важном
    menu = [By.XPATH, ".//*[@class='accordion']"]  # Гармошка с вопросами и ответами
    questions_menu = [By.XPATH, ".//*[contains(@id, 'accordion__heading-')]"]  # Список вопросов
    answers_menu = [By.XPATH, ".//*[contains(@id, 'accordion__panel-')]/p"]  # Список ответов
    accept_cookies = [By.XPATH, ".//button[@class='App_CookieButton__3cvqF' and text()='да все привыкли']"]  # Кнопка согласия с куки
    button_order_up = [By.XPATH, ".//*[@class='Button_Button__ra12g']"]  # Кнопка заказа на основной странице
    button_order_down = [By.XPATH, ".//*[contains(@class, 'Button_Middle__1CSJM')]"]  # Кнопка заказа снизу
    button_scooter = [By.XPATH, ".//*[@alt='Scooter']"]  # Логотип Скутер
    button_yandex = [By.XPATH, ".//*[@alt='Yandex']"]  # Логотип Яндекс
    element_from_yandex = [By.XPATH, ".//iframe[@class='dzen-search-arrow-common__frame' and @aria-label='Поиск Яндекса']"]  # Поисковая строка на странице Яндекс Дзен


class OrderPageLocators:
    field_name = [By.XPATH, ".//*[@placeholder='* Имя']"]  # Поле имени
    field_last_name = [By.XPATH, ".//*[@placeholder='* Фамилия']"]  # Поле Фамилии
    field_address = [By.XPATH, ".//*[@placeholder='* Адрес: куда привезти заказ']"]  # Поле адреса
    field_phone_number = [By.XPATH, ".//*[@placeholder='* Телефон: на него позвонит курьер']"]  # Поле номера телефона
    field_subway_station = [By.XPATH, ".//*[@placeholder='* Станция метро']"]  # Поле выбора метро
    button_next = [By.XPATH, ".//*[text()='Далее']"]  # Кнопка Далее
    field_when_to_bring = [By.XPATH, ".//*[@placeholder='* Когда привезти самокат']"]  # Поле выбора даты доставки
    field_rental_period = [By.XPATH, ".//*[@class='Dropdown-arrow']"]  # Выбор срока аренды
    rental_period_menu = [By.XPATH, ".//*[@class='Dropdown-menu']/div"]  # Список срока аренды
    field_scooter_color = [By.XPATH, ".//*[@class='Checkbox_Label__3wxSf']"]  # Поле выбора цвета самоката
    field_comment = [By.XPATH, ".//*[@placeholder='Комментарий для курьера']"]  # Поле комментария для курьера
    button_to_order = [By.XPATH, ".//*[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') "
                                 "and text()='Заказать']"]  # Кнопка Заказать на странице заказа
    yes_or_no_buttons = [By.XPATH, ".//*[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM')""and text()='Нет'or text()='Да']"]  # Кнопки ответов Да или Нет

    info_about_order = [By.XPATH, ".//*[@class='Order_ModalHeader__3FDaJ']"]  # Информация о статусе заказа
