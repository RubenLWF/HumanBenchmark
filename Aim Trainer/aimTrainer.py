from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('log-level=3')

browser = webdriver.Chrome(options=options)

url = "https://humanbenchmark.com/tests/aim"
browser.get(url)

print('Ready to start?')
startWait = input()

actions = ActionChains(browser)
i = 0
while i <= 30:
    actions.move_to_element(browser.find_element(By.CSS_SELECTOR, '#root > div > div:nth-child(4) > div.css-12ibl39.e19owgy77 > div > div.desktop-only > div > div > div')).click().perform()
    i += 1