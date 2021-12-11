import time
from selenium.webdriver.common.by import By

def test_see_button_add(browser): 
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)

    add = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert add is not None, 'кнопка "Добавить в корзину" не найдена'


