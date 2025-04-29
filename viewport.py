from selenium import webdriver
import time

viewports = [(1024, 768), (768, 1024), (375, 667), (412, 915)]

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

#driver.set_window_size(768, 1024)

try:
    for width, height in viewports:
        driver.set_window_size(width, height)
        time.sleep(5)
        
finally:
    driver.close()