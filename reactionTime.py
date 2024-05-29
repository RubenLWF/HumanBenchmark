from selenium import webdriver
from selenium.webdriver.common.by import By
from screeninfo import get_monitors
import mouse
import mss.tools
import time

def reactionTime():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('log-level=3')

    mainMonitor = get_monitors()[0]
    monitorWidth = mainMonitor.width
    monitorHeight = mainMonitor.height

    browser = webdriver.Chrome(options=options)
    browser.set_window_position(monitorWidth/2, 0)
    browser.set_window_size(monitorWidth/2, monitorHeight-30)
    window = browser.get_window_position()

    url = "https://humanbenchmark.com/tests/reactiontime"
    browser.get(url)

    input('Ready to start? ')

    div = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div')
    location = div.location
    size = div.size
    x = window['x'] + location['x']
    y = window['y'] + location['y'] + 131
    monitor = {"top": y + 10, "left": x + 10, "width": 1, "height": 1}

    i = 0
    while i <= 4:
        if (mss.mss().grab(monitor).pixel(0,0) == (70, 205, 99)):
            mouse.click()
            time.sleep(0.5)
            mouse.click()
            i += 1

    input("Press enter to exit...")
    browser.close()