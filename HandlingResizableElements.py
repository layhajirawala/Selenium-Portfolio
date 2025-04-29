import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()
url = "https://demo.automationtesting.in/Resizable.html"
browser.get(url)

time.sleep(3)

resizable_image = browser.find_element(By.CSS_SELECTOR, "#resizable")

corner_element = browser.find_element(By.CSS_SELECTOR, ".ui-resizable-handle.ui-resizable-se.ui-icon.ui-icon-gripsmall-diagonal-se")

initial_size = resizable_image.size
print(f"Initial size: {initial_size}")

actions = ActionChains(browser)
# Click on the corner, resize.
actions.click_and_hold(corner_element).move_by_offset(100, 100).release().perform()
time.sleep(3)
new_size = resizable_image.size
print(f"New size: {new_size}")

time.sleep(3)
browser.quit()