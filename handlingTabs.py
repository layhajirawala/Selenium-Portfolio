from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://www.selenium.dev/")
browser.switch_to.new_window()
browser.get("https://playwright.dev/")

# Number of tabs
number_of_tabs = len(browser.window_handles)
print(number_of_tabs)

# Unique value of each tab.
tab_value = browser.window_handles
print(tab_value)

# Current tab value.
current_tab = browser.current_window_handle
print(current_tab)

# Click on current tab.
browser.find_element(By.CSS_SELECTOR, ".getStarted_Sjon").click()

# Switch to first tab.
first_tab = browser.window_handles[0]

if current_tab != first_tab:
    browser.switch_to.window(first_tab)
browser.find_element(By.XPATH, "//span[normalize-space()='Projects']").click()