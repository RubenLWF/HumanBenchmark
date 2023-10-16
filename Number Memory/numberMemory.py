from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('log-level=3')

browser = webdriver.Chrome(options=options)

url = "https://humanbenchmark.com/tests/number-memory"
browser.get(url)

print('Ready to start?')
startWait = input()

start = browser.find_element(By.XPATH, '//button[text()="Start"]')
start.click()

i = 0
while (i < 99):
    number = browser.find_element(By.CLASS_NAME, 'big-number ').text
    while len(browser.find_elements(By.XPATH, "//input[@type='text']")) == 0:
        pass
    browser.find_element(By.XPATH, "//input[@type='text']").send_keys(number)
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()
    print(i)
    browser.find_element(By.XPATH, '//button[text()="NEXT"]').click()
    i += 1