import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

load_dotenv("./selenium/linkedin/.env")
PASS = os.getenv("PASS") 
USER = os.getenv("USER")
print(USER)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

webdriver = webdriver.Chrome(options=options)
webdriver.maximize_window()
webdriver.get("https://www.linkedin.com/feed/")
webdriver.implicitly_wait(10)

username = webdriver.find_element(By.ID, "username")
password = webdriver.find_element(By.ID, "password")

username.send_keys(USER)
password.send_keys(PASS)
password.send_keys(Keys.ENTER)

print("QUICK!!! solve the captcha ╰(*°▽°*)╯")

top_bar = webdriver.find_element(By.CSS_SELECTOR, ".global-nav__nav ul")
elements = top_bar.find_elements(By.TAG_NAME, "li")
jobs = elements[2].click()


search = webdriver.find_element(By.CSS_SELECTOR, ".jobs-search-box__input .jobs-search-box__inner input")
search.send_keys("data analyst")
search.send_keys(Keys.ENTER)


filters = webdriver.find_elements(By.CSS_SELECTOR, ".grid li")
for filter in filters:
    if filter.text == "Remote":
        filter.click()
        options = filter.find_elements(By.CSS_SELECTOR, ".pl4 ul p")
        for option in options:
            if "Remote" in option.text:
                option.click()

    if filter.text == "Easy Apply":
        filter.click() 

time.sleep(1)

all_listings = webdriver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

job_results = webdriver.find_elements(By.CSS_SELECTOR, ".jobs-search-results-list ul li")
for job in job_results:
    job.click()
    time.sleep(4)