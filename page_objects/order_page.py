from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class OrderPage(BasePage):

    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.CLASS_NAME, 'select-search__input')
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CLASS_NAME, 'Dropdown-control')
    COLOR_BLACK = (By.ID, 'black')
    COLOR_GREY = (By.ID, 'grey')
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']")
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class,'Order_ModalHeader')]")

    def fill_step_one(self, name, surname, address, metro, phone):
        self.fill(self.NAME_INPUT, name)
        self.fill(self.SURNAME_INPUT, surname)
        self.fill(self.ADDRESS_INPUT, address)

        self.fill(self.METRO_INPUT, metro)
        self.click((
            By.XPATH,
            f"//div[contains(@class,'select-search__select')]//div[text()='{metro}']"
        ))

        self.fill(self.PHONE_INPUT, phone)

    def click_next(self):
        self.click(self.NEXT_BUTTON)

    def fill_step_two(self, date, rental_period, color=None, comment=None):
        self.fill(self.DATE_INPUT, date)

        self.click((By.TAG_NAME, "body"))

        self.click(self.RENTAL_PERIOD)
        self.click((By.XPATH, f"//div[contains(text(),'{rental_period}')]"))

        if color == "black":
            self.click(self.COLOR_BLACK)
        elif color == "grey":
            self.click(self.COLOR_GREY)

        if comment:
            self.fill(self.COMMENT_INPUT, comment)

    def click_order(self):
        self.click(self.ORDER_BUTTON)

    def confirm_order(self):
        self.click(self.CONFIRM_YES_BUTTON)

    def is_success_visible(self):
        return self.is_visible(self.SUCCESS_MODAL)