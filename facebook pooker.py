from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

aClass="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f"

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

#add names that you want to poke back
pokeList = ["name 1","name 2","name 3"]

# Go to the Facebook login page
driver.get("https://www.facebook.com/")

# Find the email and password fields and enter your login details
email_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "pass")
email_field.send_keys("your email")
password_field.send_keys("your password")
password_field.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(5)

while True:
    # Go to the pokes page
    driver.get("https://www.facebook.com/pokes")

    # Use BeautifulSoup to parse the page HTML
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    name_elements = soup.find_all('a', class_=aClass)

    # Loop through the name elements
    for name_element in name_elements:
        name_text = name_element.get_text()
        print("Poking " + name_text+" back")
        # Wait for the page to load
        time.sleep(1)            # Find the Poke Back button of the current name element
        poke_back_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Poke Back')]")
        # Click the Poke Back button
        ActionChains(driver).move_to_element(poke_back_button).click(poke_back_button).perform()

    # Wait for 30 seconds before reloading the page
    time.sleep(1)