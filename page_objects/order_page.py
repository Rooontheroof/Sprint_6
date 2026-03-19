from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:

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

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_step_one(self, name, surname, address, metro, phone):
        self.wait.until(EC.visibility_of_element_located(self.NAME_INPUT)).send_keys(name)
        self.wait.until(EC.visibility_of_element_located(self.SURNAME_INPUT)).send_keys(surname)
        self.wait.until(EC.visibility_of_element_located(self.ADDRESS_INPUT)).send_keys(address)

        metro_input = self.wait.until(EC.visibility_of_element_located(self.METRO_INPUT))
        metro_input.send_keys(metro)

        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[text()='{metro}']"))
        ).click()

        self.wait.until(EC.visibility_of_element_located(self.PHONE_INPUT)).send_keys(phone)

    def click_next(self):
        self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON)).click()

    def fill_step_two(self, date, rental_period, color=None, comment=None):
        date_input = self.wait.until(EC.visibility_of_element_located(self.DATE_INPUT))
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys("\n")

        self.driver.find_element(By.TAG_NAME, "body").click()
        self.wait.until(EC.element_to_be_clickable(self.RENTAL_PERIOD)).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(),'{rental_period}')]"))).click()

        if color == "black":
            self.wait.until(EC.element_to_be_clickable(self.COLOR_BLACK)).click()
        elif color == "grey":
            self.wait.until(EC.element_to_be_clickable(self.COLOR_GREY)).click()

        if comment:
            self.wait.until(EC.visibility_of_element_located(self.COMMENT_INPUT)).send_keys(comment)

    def click_order(self):
        self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON)).click()

    def confirm_order(self):
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_YES_BUTTON)).click()

    def is_success_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MODAL)).is_displayed()
    