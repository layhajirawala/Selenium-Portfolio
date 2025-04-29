from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
browser.maximize_window()

browser.execute_script("window.scrollBy(0, 500);")
#browser.find_element(By.XPATH, "//label[normalize-space()='Sunday']").click()
#time.sleep(5)
#browser.find_element(By.XPATH, "//label[normalize-space()='Sunday']").click()

# Check all the checkboxes.
checkboxes = browser.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)

checked_count = 0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count += 1

expected_count = 7

if checked_count == expected_count:
    print('Checkbox count verified')
else:
    print('Checkbox count mismatch')

time.sleep(5)
browser.close()

