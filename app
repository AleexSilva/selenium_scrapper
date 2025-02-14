import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def search_on_duckduckgo(search_terms):
    chrome_options = Options()
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/237.84.2.178 Safari/537.36")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://duckduckgo.com")
    time.sleep(1)
    search_box = driver.find_element(By.ID, "search_form_input_homepage")
    search_box.click()
    search_box.send_keys(search_terms)
    search_box.send_keys(Keys.RETURN)
    time.sleep(1)
    driver.quit()