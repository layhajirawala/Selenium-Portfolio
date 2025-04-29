from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://selenium.dev/")
browser.maximize_window()       # maximize window method
title = browser.title
print(title)

assert "Selenium" in title

