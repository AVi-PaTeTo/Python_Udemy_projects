import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=C:")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.set_window_size(height=900,width=300)
driver.get("https://tinder.com/")


decline = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="q-856107901"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button')))
decline.click()

for x in range(100):
    swipe = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="q-856107901"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[4]/button')))
    swipe.click()                                                                     
    time.sleep(2)                                                                      
    print("swiped")                                                                     
