from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    URL = 'https://qa-scooter.praktikum-services.ru/'

    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']")

    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")

    FAQ_SECTION = (By.CLASS_NAME, 'Home_FAQ__3uVm4')
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def accept_cookies(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.COOKIE_BUTTON)).click()
        except:
            pass

    def scroll_to_faq(self):
        faq = self.wait.until(EC.presence_of_element_located(self.FAQ_SECTION))
        self.driver.execute_script("arguments[0].scrollIntoView();", faq)

    def click_faq_question(self, index):
        locator = (By.ID, f'accordion__heading-{index}')
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_faq_answer_text(self, index):
        locator = (By.XPATH, f"//div[@id='accordion__panel-{index}']//p")
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def click_order_button(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_scooter_logo(self):
        self.wait.until(EC.element_to_be_clickable(self.SCOOTER_LOGO)).click()

    def click_yandex_logo(self):
        self.wait.until(EC.element_to_be_clickable(self.YANDEX_LOGO)).click()

    def switch_to_new_tab(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def is_main_page(self):
        return "praktikum-services" in self.driver.current_url