from datetime import datetime, timedelta
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
url = "https://www.globalsqa.com/demo-site/datepicker/#Simple%20Date%20Picker"
browser.get(url)

# Closing the Pick a date prompt.
browser.find_element(By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//a[@class='close_img']").click()

# Date picker is in iframe, we have to switch to iframe.
iframe = browser.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']")
browser.switch_to.frame(iframe)

# Datepicker
browser.find_element(By.CSS_SELECTOR, "#datepicker").click()

current_date = datetime.now()

next_date = current_date + timedelta(days=1)

formatted_date = current_date.strftime("%m/%d/%Y")
browser.find_element(By.CSS_SELECTOR, "#datepicker").send_keys(formatted_date + Keys.TAB)

time.sleep(5)
browser.close()