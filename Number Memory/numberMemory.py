import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
#import pyautogui

global browser
browser = webdriver.Chrome()

url = "https://humanbenchmark.com/tests/number-memory"
browser.get(url)

print('Ready to start?')
test = input()

page_source = browser.page_source

start = browser.find_element(By.XPATH, '//button[text()="Start"]')
start.click()

i = 0
while (i < 99):
    number = browser.find_element(By.CLASS_NAME, 'big-number ').text
    while len(browser.find_elements(By.XPATH, "//input[@type='text']")) == 0:
        pass
    browser.find_element(By.XPATH, "//input[@type='text']").send_keys(number)
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()
    browser.find_element(By.XPATH, '//button[text()="NEXT"]').click()
    i += 1
    
print('Close window?')
x = input()