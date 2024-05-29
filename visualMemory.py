from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def visualMemory():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('log-level=3')

    browser = webdriver.Chrome(options=options)
    browser.set_window_position(1270, 0)
    browser.set_window_size(1300, 1050)

    url = "https://humanbenchmark.com/tests/memory"
    browser.get(url)

    stopScore = input('What score do you want to go to? ')
    input('Ready to start? (Make sure you\'re logged in) ')

    browser.find_element(By.XPATH, '//button[text()="Start"]').click()

    time.sleep(1)

    i = 0
    while (i < int(stopScore) - 1):
        active = browser.find_elements(By.XPATH, "//div[contains(@class, 'active')]")

        time.sleep(1.5)

        for a in active:
            a.click()

        while len(browser.find_elements(By.XPATH, "//span[text()='{level}']".format(level = str(i + 2)))) == 0:
            pass
        
        time.sleep(0.5)

        i += 1

    input("Press enter to exit...")
    browser.close()