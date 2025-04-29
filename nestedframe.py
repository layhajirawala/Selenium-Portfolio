import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/nested_frames")

# Switch to Top frame.
top_frame = browser.find_element(By.NAME, "frame-top")
browser.switch_to.frame(top_frame)

# Switch to Middle frame.
middle_frame = browser.find_element(By.NAME, "frame-middle")
browser.switch_to.frame(middle_frame)
content = browser.find_element(By.ID, "content").text
print(f"Content in Middle frame: {content}")

# We have to switch to default content before switching to Bottom frame.
browser.switch_to.default_content()

# Switch to Bottom frame.
bottom_frame = browser.find_element(By.NAME, "frame-bottom")
browser.switch_to.frame(bottom_frame)
content_bottom = browser.find_element(By.TAG_NAME, "body").text
print(f"Content in Bottom frame: {content_bottom}")

time.sleep(3)
browser.quit()