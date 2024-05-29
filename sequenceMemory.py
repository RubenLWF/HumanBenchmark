from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('log-level=3')

browser = webdriver.Chrome(options=options)
browser.set_window_position(1270, 0)
browser.set_window_size(1300, 1050)

url = "https://humanbenchmark.com/tests/sequence"
browser.get(url)

stopScore = input('What score do you want to go to? ')
input('Ready to start?')

browser.find_element(By.XPATH, '//button[text()="Start"]').click()

i = 0
while (i < int(stopScore) - 1):
    activeCells = []

    j = 0
    while (j < i + 1):
        active = browser.find_elements(By.XPATH, "//div[contains(@class, 'active')]")

        if (len(active) == 1):
            activeCells.append(active[0])
            time.sleep(0.5)
            j += 1

    for cell in activeCells:
        cell.click()

    while len(browser.find_elements(By.XPATH, "//span[text()='{level}']".format(level = str(i + 2)))) == 0:
        pass

    i += 1

input("Press enter to exit...")