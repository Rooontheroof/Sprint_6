import pytest
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage


ORDER_DATA = [
    (
        'Иван', 'Иванов',
        'ул. Ленина, 1', 'Черкизовская', '+79161234567',
        '10.06.2025', 'двое суток', 'black', 'Позвоните за час'
    ),
    (
        'Мария', 'Петрова',
        'пр. Мира, 42', 'Сокольники', '+79269876543',
        '20.06.2025', 'сутки', 'grey', ''
    ),
]


class TestOrderScooter:

    @pytest.mark.parametrize("button", [
        MainPage.ORDER_BUTTON_TOP,
        MainPage.ORDER_BUTTON_BOTTOM
    ])
    @pytest.mark.parametrize("data", ORDER_DATA)
    def test_order_success(self, driver, button, data):
        page = MainPage(driver)
        page.open()

        page.accept_cookies()

        page.click_order_button(button)

        page.accept_cookies()

        order = OrderPage(driver)

        order.fill_step_one(*data[:5])
        order.click_next()

        order.fill_step_two(*data[5:])
        order.click_order()
        order.confirm_order()

        assert order.is_success_visible()

    def test_scooter_logo(self, driver):
        page = MainPage(driver)
        page.open()

        page.click_scooter_logo()

        assert page.is_main_page()

    def test_yandex_logo(self, driver):
        page = MainPage(driver)
        page.open()

        page.click_yandex_logo()

        page.wait.until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[-1])

        page.wait.until(lambda d: d.current_url != "about:blank")

        assert "yandex" in driver.current_url or "dzen" in driver.current_url