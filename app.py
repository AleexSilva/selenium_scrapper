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
    
    global_reuslts = []
    
    for term in search_terms:
        time.sleep(random.randint(1,5))

        driver.get("https://duckduckgo.com/")        
        driver.maximize_window()
    
        #search box
        search_box = driver.find_element(By.NAME,"q")
        search_box.send_keys(term)
        search_box.send_keys(Keys.RETURN)    
        
        time.sleep(random.randint(1,5))
        
        results = driver.find_elements(By.CSS_SELECTOR,"h2 a")
        for result in results:
            try:
                title = result.text
                link = result.get_attribute("href")
                if title and link:   
                    global_reuslts.append({
                        "Term": term,
                        "Title": title,
                        "Link": link
                    })
            except Exception:
                continue

