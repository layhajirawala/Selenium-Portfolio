import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

current_dir = os.path.dirname(os.path.abspath(__file__))

people = [
    {
      'first_name': 'Peter',
      'last_name': 'Parker',
      'email': 'peter.parker@gmail.com',
      'gender': 'Male',
      'mobile': '9876543210',
      'dob': '10 Aug 2001',
      'subject': 'Chemistry',
      'hobbies': ['Reading', 'Music'],
      'picture': os.path.join(current_dir, 'peter.jpeg'),
      'current_address': '20 Ingram Street, Queens, New York',
      'state': 'NCR',
      'city': 'Delhi'
    },
    {
      'first_name': 'Mary',
      'last_name': 'Jane',
      'email': 'mary.jane@gmail.com',
      'gender': 'Female',
      'mobile': '2345678910',
      'dob': '19 Aug 2000',
      'subject': 'Arts',
      'hobbies': ['Sports'],
      'picture': os.path.join(current_dir, 'mj.jpeg'),
      'current_address': '100 Main Street, Manhattan, New York',
      'state': 'NCR',
      'city': 'Delhi'
    }
]

url = 'https://demoqa.com/automation-practice-form'
options = webdriver.FirefoxOptions()
browser = webdriver.Firefox(options=options)
browser.maximize_window()
browser.get(url)
browser.implicitly_wait(10)
wait = WebDriverWait(browser, 10)

def sleep():
    time.sleep(5)


for person in people:
  # Enter first name.
  browser.find_element(By.CSS_SELECTOR, '#firstName').clear()
  browser.find_element(By.CSS_SELECTOR, '#firstName').send_keys(person['first_name'])
  
  # Enter last name.
  browser.find_element(By.ID, 'lastName').clear()
  browser.find_element(By.ID, 'lastName').send_keys(person['last_name'])
  
  # Enter email.
  browser.find_element(By.XPATH, "//input[@id='userEmail']").clear()
  browser.find_element(By.XPATH, "//input[@id='userEmail']").send_keys(person['email'])
  
  # Select gender.
  gender_xpath = f"//label[normalize-space()='{person['gender']}']"
  browser.find_element(By.XPATH, gender_xpath).click()
  
  # Enter mobile num.
  browser.find_element(By.CSS_SELECTOR, "#userNumber").clear()
  browser.find_element(By.CSS_SELECTOR, "#userNumber").send_keys(person['mobile'])
  
  # Scroll down. 
  browser.execute_script("window.scrollBy(0, 300)")
  
  sleep()
  
  # Date of birth.
  dob_element = browser.find_element(By.XPATH, "//input[@id='dateOfBirthInput']")
  dob_element.click()
  dob_element.send_keys(Keys.CONTROL + "a")
  dob_element.send_keys(person['dob'])
  dob_element.send_keys(Keys.ENTER)
  
  # Select subjects.
  subject_element = browser.find_element(By.ID, "subjectsInput")
  subject_element.send_keys(person['subject'])
  time.sleep(3)
  subject_element.send_keys(Keys.ENTER)
  
  sleep()
  
  # Scroll down. 
  #browser.execute_script("window.scrollBy(0, 300)")
  
  
  sleep()
  
  # Select hobbies.
  for hobby in person['hobbies']:
    hobby_xpath = f"//label[normalize-space()='{hobby}']"     #//label[normalize-space()='Reading']
    hobby_element = browser.find_element(By.XPATH, hobby_xpath)
    browser.execute_script("arguments[0].scrollIntoView(true);", hobby_element)
    sleep()
    print("Trying to click hobby:", hobby_element)
    hobby_element.click()
    
  # Upload picture.
  browse_id = "uploadPicture"
  browse_element = browser.find_element(By.ID, browse_id)
  
  picture_path = person['picture']
  if os.path.exists(picture_path):
    browse_element.send_keys(person['picture'])
  else:
    print(f"File not found: {picture_path}")
    
  # Enter address.
  address_element = browser.find_element(By.ID, 'currentAddress')
  address_element.clear()
  address_element.send_keys(person['current_address'])
  
  # Select state.
  browser.find_element(By.XPATH, "//div[contains(text(),'Select State')]").click()
  state_option_xpath = f"//div[contains(@id, 'react-select-3-option-') and text()='{person['state']}']"
  wait.until(EC.element_to_be_clickable((By.XPATH, state_option_xpath))).click()
  
  # Select city.
  browser.find_element(By.XPATH, "//div[contains(text(),'Select City')]").click()
  city_option_xpath = f"//div[contains(@id, 'react-select-4-option-') and text()='{person['city']}']"
  wait.until(EC.element_to_be_clickable((By.XPATH, city_option_xpath))).click()

  # Submit.
  browser.find_element(By.ID, 'submit').click()

  # Close.

  # Find the pop-up.
  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#example-modal-sizes-title-lg")))

  close_button = browser.find_element(By.CSS_SELECTOR, '#closeLargeModal')

  # Button obstructed by an ad.
  browser.execute_script("arguments[0].click();", close_button)   # forcing clicking on close button

  sleep()
  
browser.quit()
  
  

