import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors-spki-list')

browser = webdriver.Chrome(options=options)

url = "https://humanbenchmark.com/tests/verbal-memory"
browser.get(url)

print('Ready to start?')
test = input()

page_source = browser.page_source

start = browser.find_element(By.XPATH, '//button[text()="Start"]')
start.click()

seen = browser.find_element(By.XPATH, '//button[text()="SEEN"]')
new = browser.find_element(By.XPATH, '//button[text()="NEW"]')
words = []
seenWord = False

i = 0
while (i <= 999):
    word = browser.find_element(By.CLASS_NAME, "word").text
    for x in words:
        if x == word:
            seenWord = True
    if seenWord:
        seen.click()
        seenWord = False
    else:
        words.append(word)
        new.click()
        seenWord = False
    i += 1