import allure
from selenium.webdriver.common.by import By
from .BasePage import BasePage


class MainPage(BasePage):
    URL = 'https://qa-scooter.praktikum-services.ru/'

    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']")

    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")

    FAQ_SECTION = (By.CLASS_NAME, 'Home_FAQ__3uVm4')
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    @allure.step("Открыть главную страницу")
    def open_page(self):
        self.open(self.URL)

    @allure.step("Принять cookies")
    def accept_cookies(self):
        self.click_if_clickable(self.COOKIE_BUTTON)

    @allure.step("Прокрутка к FAQ")
    def scroll_to_faq(self):
        self.scroll_to(self.FAQ_SECTION)

    @allure.step("Клик по вопросу FAQ {index}")
    def click_faq_question(self, index):
        locator = (By.ID, f'accordion__heading-{index}')
        self.click(locator)

    @allure.step("Получить текст ответа FAQ {index}")
    def get_faq_answer_text(self, index):
        locator = (By.XPATH, f"//div[@id='accordion__panel-{index}']//p")
        return self.get_text(locator)

    @allure.step("Клик по кнопке заказа")
    def click_order_button(self, locator):
        if locator == self.ORDER_BUTTON_BOTTOM:
            self.scroll_to(locator)
        self.click(locator)

    @allure.step("Клик по логотипу Scooter")
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    @allure.step("Клик по логотипу Yandex")
    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)

    @allure.step("Проверка, что открыта главная страница")
    def is_main_page(self):
        return "praktikum-services" in self.get_current_url()