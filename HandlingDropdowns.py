from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox()
driver.maximize_window()
login_url = 'https://the-internet.herokuapp.com/dropdown'
driver.get(login_url)

dropdown_element = driver.find_element(By.ID, "dropdown")
target_value = "Option 2"
dropdown = Select(dropdown_element)

for option in dropdown.options:
    if option.text == target_value:
        option.click()
        print(f"Selected option is {target_value}")
        break
else:
    print(f"{target_value} not found!")
        
#dropdown = Select(dropdown_element)

#option_count = len(dropdown.options)

#expected_count = 3

#if option_count == expected_count:
    #print("Incorrect count.")
#else:
    #print("Correct count.")
    
# Select the value by visible text
# Select the value by Index
# Select the value by using a value

#dropdown.select_by_visible_text("Option 2")
#dropdown.select_by_index(2)
#dropdown.select_by_value("2")
time.sleep(2)
driver.close()



