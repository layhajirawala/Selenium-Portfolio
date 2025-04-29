import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.saucedemo.com/"

browser = webdriver.Firefox()
browser.maximize_window()
browser.implicitly_wait(10)
browser.get(url)

browser.find_element(By.CSS_SELECTOR, "#user-name").send_keys('standard_user')
browser.find_element(By.XPATH, "//input[@id='password']").send_keys('secret_sauce')
browser.find_element(By.CSS_SELECTOR, "#login-button").click()
time.sleep(5)
browser.find_element(By.CSS_SELECTOR, "#react-burger-menu-btn").click()
browser.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()

time.sleep(3)
browser.quit()



