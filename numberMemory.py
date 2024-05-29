from selenium import webdriver
from screeninfo import get_monitors
from selenium.webdriver.common.by import By

def numberMemory():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('log-level=3')

    mainMonitor = get_monitors()[0]
    monitorWidth = mainMonitor.width
    monitorHeight = mainMonitor.height

    browser = webdriver.Chrome(options=options)
    browser.set_window_position(monitorWidth/2, 0)
    browser.set_window_size(monitorWidth/2, monitorHeight-30)

    url = "https://humanbenchmark.com/tests/number-memory"
    browser.get(url)

    stopScore = input('What score do you want to go to? ')
    input('Ready to start? (Make sure you\'re logged in) ')

    browser.find_element(By.XPATH, '//button[text()="Start"]').click()

    i = 0
    while (i < int(stopScore)):
        number = browser.find_element(By.CLASS_NAME, 'big-number ').text
        while len(browser.find_elements(By.XPATH, "//input[@type='text']")) == 0:
            pass
        browser.find_element(By.XPATH, "//input[@type='text']").send_keys(number)
        browser.find_element(By.XPATH, '//button[text()="Submit"]').click()
        browser.find_element(By.XPATH, '//button[text()="NEXT"]').click()
        i += 1

    input("Press enter to exit...")
    browser.close()