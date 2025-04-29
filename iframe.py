import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/iframe")

# Switching to iframe from main browser
iframe = browser.find_element(By.ID, "mce_0_ifr")
browser.switch_to.frame(iframe)

# Switching to text editor from iframe
text_editor = browser.find_element(By.ID, "tinymce")
text_editor.clear()
text_editor.send_keys("Selenium with Python learning practice.")

# We want to click on the link outside the iframe.
# Switch to browser (default content).
browser.switch_to.default_content()
browser.find_element(By.XPATH, "//a[normalize-space()='Elemental Selenium']").click()
time.sleep(3)