import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/broken_images"
browser.get(url)
browser.maximize_window()

images = browser.find_elements(By.TAG_NAME, "img")
broken_images = []

for image in images:
    source = image.get_attribute("src")
    if source:
        response = requests.get(source)
        if response.status_code == 404:
            broken_images.append(source)
            print("Broken Image Found")

if broken_images:
    print("List of Broken Images:")
    for broken_image in broken_images:
        print(broken_image)

else:
    print("No Broken Images Found")

