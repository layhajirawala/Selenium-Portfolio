import time

from selenium import webdriver


username = "admin"
password = "admin"

browser = webdriver.Firefox()
browser.maximize_window()
url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
browser.get(url)

time.sleep(5)
browser.close()

#https://username:password@domain/path