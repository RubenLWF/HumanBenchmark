from selenium import webdriver
from screeninfo import get_monitors
from selenium.webdriver.common.by import By

def verbalMemory():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('log-level=3')

    mainMonitor = get_monitors()[0]
    monitorWidth = mainMonitor.width
    monitorHeight = mainMonitor.height

    browser = webdriver.Chrome(options=options)
    browser.set_window_position(monitorWidth/2, 0)
    browser.set_window_size(monitorWidth/2, monitorHeight-30)

    url = "https://humanbenchmark.com/tests/verbal-memory"
    browser.get(url)

    stopScore = input('What score do you want to go to? ')
    input('Ready to start? (Make sure you\'re logged in) ')

    browser.find_element(By.XPATH, '//button[text()="Start"]').click()

    seen = browser.find_element(By.XPATH, '//button[text()="SEEN"]')
    new = browser.find_element(By.XPATH, '//button[text()="NEW"]')
    words = []
    seenWord = False

    i = 0
    while (i <= int(stopScore)):
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

    input("Press enter to exit...")
    browser.close()