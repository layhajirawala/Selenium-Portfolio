import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()
url = "https://demo.automationtesting.in/Datepicker.html"
browser.get(url)

actions = ActionChains(browser)

time.sleep(3)

hover_to = browser.find_element(By.XPATH, "//a[normalize-space()='SwitchTo']")
actions.move_to_element(hover_to).perform()
hover_to_element2 = browser.find_element(By.XPATH, "//a[normalize-space()='Frames']")
actions.move_to_element(hover_to_element2).click().perform()

time.sleep(3)
browser.quit()