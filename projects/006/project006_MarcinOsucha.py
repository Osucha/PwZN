from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file_name", type=str, default="output", help="name of the output file")
args = parser.parse_args()

url = 'https://www.imdb.com/'

options = Options()
service = Service('projects/webdriver/chromedriver.exe')

driver = webdriver.Chrome(service=service, options=options)
driver.get(url)

button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#__next > div > div > div.sc-jrcTuL.bPmWiM > div > button.icb-btn.sc-bcXHqe.sc-dkrFOg.sc-iBYQkv.dcvrLS.ddtuHe.dRCGjd')))
button.click()

for _ in range(6):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)

container = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center.sc-a10d778f-0.hmZTRy > div:nth-child(11) > div > section:nth-child(5) > div > div.sc-e3008202-0.ghlkuX > div'))
)

items = container.find_elements(By.CSS_SELECTOR, "a.name-born-today-card")
birthdays = {}

for item in items:
    try:
        name = item.find_element(By.CSS_SELECTOR, "div.sc-def41e7-1.FIZtP.born-today-name").text
        age = item.find_element(By.CSS_SELECTOR, "div.sc-def41e7-0.esDiD.born-today-age").text
        
        birthdays[name] = age
    except Exception as e:
        # print(f"Element pominięty: {e}")
        age = "<UNKNOWN>"
        birthdays[name] = age

file_name = 'projects/006/output/' + args.file_name + '.json'
print(f'Saving data to {file_name}')

with open(file_name, 'w') as file:
    json.dump(birthdays, file, indent=4)

time.sleep(5000)
driver.close()