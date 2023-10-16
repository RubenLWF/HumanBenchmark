from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('log-level=3')

browser = webdriver.Chrome(options=options)

url = "https://humanbenchmark.com/tests/typing"
browser.get(url)

print('Ready to start?')
startWait = input()

text = browser.find_element(By.XPATH, './/span[@class = "incomplete current"]').text

for letter in browser.find_elements(By.XPATH, './/span[@class = "incomplete"]'):
    if letter.text == "":
        text = text + " "
    else:
        text = text + letter.text

browser.find_element(By.XPATH, './/div[@class = "letters notranslate"]').send_keys(text)