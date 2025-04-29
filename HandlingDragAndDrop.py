import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
url = "https://the-internet.herokuapp.com/drag_and_drop"
browser.get(url)

actions = ActionChains(browser)

item_a = browser.find_element(By.CSS_SELECTOR, "#column-a")
item_b = browser.find_element(By.XPATH, "//div[@id='column-b']")

time.sleep(3)

actions.move_to_element(item_a).perform()   # Hover to Item A
time.sleep(3)
actions.drag_and_drop(item_a, item_b).perform()     # Moving Item A to Item B

time.sleep(5)
browser.quit()