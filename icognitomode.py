import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
# Chrome
chrome_options = ChromeOptions()
chrome_options.add_argument("--incognito")
browser_chrome = webdriver.Chrome(chrome_options)
browser_chrome.maximize_window()
browser_chrome.get("https://www.google.com")

time.sleep(3)
browser_chrome.close()

time.sleep(10)

# Firefox
firefox_options = FirefoxOptions()
firefox_options.add_argument("--private")
browser_firefox = webdriver.Firefox(firefox_options)
browser_firefox.maximize_window()
browser_firefox.get("https://www.google.com")

time.sleep(3)
browser_firefox.close()