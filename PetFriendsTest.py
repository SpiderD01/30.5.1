from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_petfriends_login(browser):
    result = browser.find_element(By.CSS_SELECTOR, 'h1').text
    assert result == "PetFriends", "login error"

def test_petfriends_pets_cards(browser):
    images = browser.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = browser.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = browser.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != '', 'Image not found'
        assert names[i].text != '', 'Name not found'
        assert descriptions[i].text != '', 'Description not found'
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0, 'Species not found'
        assert len(parts[1]) > 0, 'Age not found'

def test_petfriends_card_deck(browser):
    WebDriverWait(browser, 10).until( 
        EC.presence_of_element_located((By.ID, 'navbarNav')))
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.navbar-brand.header2')))
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/my_pets"]')))
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/all_pets"]')))
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.btn.btn-outline-secondary')))
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.text-center')))
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.text-center:nth-child(2)')))
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.card-deck')))
