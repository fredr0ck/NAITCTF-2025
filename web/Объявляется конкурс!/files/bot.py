from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

def check_url(hostname, page_id):
    url = f'http://{hostname}/pages/{page_id}'

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    driver.add_cookie({
        "name": "flag", 
        "value": "NAITCTF{st34l_c00ck13s_1s_s0_e4zy}", 
        "sameSite": "Lax"
    })
    
    driver.refresh()

    WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
    
    time.sleep(3)

    driver.quit()
