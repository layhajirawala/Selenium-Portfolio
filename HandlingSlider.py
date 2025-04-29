import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
url = "https://demo.automationtesting.in/Slider.html"
browser.get(url)

time.sleep(5)

actions = ActionChains(browser)

slider = browser.find_element(By.ID, "slider")
actions.click_and_hold(slider).move_by_offset(40, 0).release().perform()
#new_position = slider.get_attribute("style")
#print(new_position)
#time.sleep(5)
#actions.click_and_hold(slider).reset_actions().release().perform()

time.sleep(3)
browser.quit()
