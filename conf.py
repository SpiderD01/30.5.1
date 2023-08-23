import pytest
from settings import email, password, base_url
from selenium.webdriver.common.by import By
from selenium import webdriver

@pytest.fixture()
def browser():
    print("\nstart browser for test")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser")
    driver.quit()


@pytest.fixture(autouse=True)
def login(browser):
    browser.implicitly_wait(10)
    browser.get(base_url)
    btn_new_user = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-success")
    btn_new_user.click()

    btn_exist_acc = browser.find_element(By.CSS_SELECTOR, "a[href='/login']")
    btn_exist_acc.click()

    field_email = browser.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys(email)

    field_pass = browser.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys(password)

    btn_submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    btn_submit.click()

    result = browser.find_element(By.CSS_SELECTOR, 'h1').text

    return result
