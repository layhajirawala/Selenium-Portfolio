import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.saucedemo.com/"

filename = 'testdata.json'

with open(filename, 'r') as f:
    test_data = json.load(f)

for data in test_data['users']:
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(url)

    time.sleep(5)

    browser.find_element(By.CSS_SELECTOR, "#user-name").send_keys(data['username'])
    browser.find_element(By.XPATH, "//input[@id='password']").send_keys(data['password'])
    browser.find_element(By.CSS_SELECTOR, "#login-button").click()
    time.sleep(2)

    browser.find_element(By.CSS_SELECTOR, "#react-burger-menu-btn").click()
    browser.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()

    time.sleep(3)

    browser.quit()



