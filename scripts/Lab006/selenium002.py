from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.9gag.com'

options = Options()
#options.add_argument('--headless')

service = Service('webdriver/chromedriver.exe')

driver = webdriver.Chrome(service=service, options=options)
driver.get(url)

# button = driver.find_element(By.CSS_SELECTOR, '#onetrust-accept-btn-handler')
# button.click()

# button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#onetrust-accept-btn-handler')))
button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#onetrust-accept-btn-handler')))
button.click()

button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#top-nav > div > div > div.general-function > a')))
button.click()

search_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#top-nav > div > div > div.general-function > div > div > form > div.ui-input > input[type=text]')))
search_field.send_keys('poland')
search_field.send_keys(Keys.ENTER)

# for _ in range(100):
#     driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)

for _ in range(100):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)

time.sleep(5000)
driver.close()