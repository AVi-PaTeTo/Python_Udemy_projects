FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScq1WTMsZk_gn6ty8vZqw9XSPBfizuccfT_DuclhPDSAqfXEQ/viewform?usp=sf_link"

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#scrape the zillow webpage
response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
zillow_html = response.text

#grabs all the apartment listings
soup = BeautifulSoup(zillow_html, "html.parser")
apartment_lists = soup.select("#grid-search-results ul .ListItem-c11n-8-84-3-StyledListCardWrapper")


#individual lists to store address, price, link
address = []
prices = []
links = []

#grab the details from every apartment and store them
for apartment in apartment_lists:

    apt_address = apartment.find("address").text.strip()
    
    #certain prices have "+" while some don't, we make sure to grab only the $price value
    apt_price_text = apartment.find("span").text
    if "+" in apt_price_text:
        apt_price = apt_price_text.split("+")[0]
    else:
        apt_price =apt_price_text.split("/")[0]

    apt_link = apartment.find("a")["href"]

    address.append(apt_address)
    prices.append(apt_price)
    links.append(apt_link)


#initiate webdriver
webdriver = webdriver.Chrome()
webdriver.maximize_window()
webdriver.get(FORM_URL)


#every loop we locate the input boxes to avoid staleException 
for index in range(len(address)):
    inputs = webdriver.find_elements(By.CSS_SELECTOR, ".Xb9hP input")

    time.sleep(1)
    address_input = inputs[0]
    address_input.send_keys(address[index])

    price_input   = inputs[1]
    price_input.send_keys(prices[index])

    link_input    = inputs[2]
    link_input.send_keys(links[index])

    submit = WebDriverWait(webdriver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".NPEfkd")))
    submit.click()

    submit_another = WebDriverWait(webdriver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".c2gzEf a")))
    submit_another.click()

