import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_should_be_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(3)
    assert browser.find_elements(By.ID, 'add_to_basket_form'), 'The cart button is not found'
