from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('log-level=3')

browser = webdriver.Chrome(options=options)

url = "https://humanbenchmark.com/tests/memory"
browser.get(url)

print('Ready to start?')
startWait = input()

start = browser.find_element(By.XPATH, '//button[text()="Start"]')
start.click()
time.sleep(1)

grid = browser.find_elements(By.XPATH, './/div[@class = "css-hvbk5q eut2yre0"]//*')
