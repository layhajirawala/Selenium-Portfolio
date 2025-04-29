import time

from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
url = "https://the-internet.herokuapp.com/javascript_alerts"
browser.get(url)

# JS alert button
jsalert = browser.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
jsalert.click()
time.sleep(3)
jsalert_prompt = browser.switch_to.alert
jsalert_prompt.accept()

browser.switch_to.default_content()

# JS Confirm button
jsconf = browser.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
jsconf.click()
time.sleep(3)
jsconf_prompt = browser.switch_to.alert
jsconf_prompt.dismiss()

browser.switch_to.default_content()

# JS Prompt button
jsprompt = browser.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
jsprompt.click()
time.sleep(3)
jsprompt_prompt = browser.switch_to.alert
jsprompt_prompt.send_keys("This is Selenium with Python tutorial for Javascript Alerts")
jsprompt_prompt.accept()
time.sleep(3)

browser.close()



