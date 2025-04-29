import time

from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.maximize_window()
url = "https://demo.automationtesting.in/Datepicker.html"
browser.get(url)


# Select Datepicker.
browser.find_element(By.CSS_SELECTOR, "#datepicker2").click()
#browser.find_element((By.ID, "datepicker2")).click()

# Date
current_date = datetime.now()
print(f"Current date: {current_date}")
current_day = (str(current_date.day))
print(f"Current day: {current_day}")

next_date = current_date + timedelta(days=1)
print(f"Tomorrow's: {next_date}")
next_day = (str(next_date.day))
print(f"Next day: {next_day}")

current_month = datetime.now().month    #current_date.month
#print(f"Current month: {current_month}")
current_year = datetime.now().year
print(f"Current year: {current_year}")

next_month = (current_month % 12) + 1
#print(f"Next month: {next_month}")

current_month_year = f"{current_month}/{current_year}"
#print(f"Current month year: {current_month_year}")

next_month_year = f"{next_month}/{current_year}"
#print(f"Next month current year: {next_month_year}")

# Select Month from Dropdown.
month_dropdown = browser.find_element(By.CSS_SELECTOR, "select[title='Change the month']")
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[title='Change the month']")))
select_month = Select(month_dropdown)
select_month.select_by_value(str(current_month_year))


#time.sleep(3)

# Select Year from Dropdown.
year_dropdown = browser.find_element(By.CSS_SELECTOR, "select[title='Change the year']")
select_year = Select(year_dropdown)
select_year.select_by_visible_text("2025")  # The demo website has the limitation, cannot select by value upon trying.

# Select Day from dropdown.
browser.find_element(By.LINK_TEXT, next_day).click()

time.sleep(5)
browser.close()