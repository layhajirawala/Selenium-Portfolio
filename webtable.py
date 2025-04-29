import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://cosmocode.io/automation-practice-webtable/")
browser.execute_script("window.scrollTo(0, 700)")
table = browser.find_element(By.ID, "countries")
rows = table.find_elements(By.TAG_NAME, "tr")
row_count = len(rows)
print(row_count)
# We'll find Maldives.
target_value = "Maldives"
found = False

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        if cell.text == target_value:
            found = True
            print(f"Found value: {target_value}")
            break

    if found:
        break
else:
    print(f"{target_value} not found")

time.sleep(4)
browser.quit()