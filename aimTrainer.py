from selenium import webdriver
from selenium.webdriver.common.by import By
from screeninfo import get_monitors
import mouse
import cv2
import mss.tools
import numpy as np
import time

def aimTrainer():
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

    url = "https://humanbenchmark.com/tests/aim"
    browser.get(url)

    stopClicks = input('How many times should be clicked? (Machine dependant) ')
    input('Ready to start? ')

    div = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[2]')
    location = div.location
    size = div.size
    w, h = size['width'], size['height']
    x = window['x'] + location['x']
    y = window['y'] + location['y'] + 131

    target = cv2.imread("img/target.jpg", 1)
    target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    target = cv2.Canny(target, 50,200)

    with mss.mss() as sct:
        monitor = {"top": y, "left": x, "width": w, "height": h}
        img = cv2.cvtColor(np.array(sct.grab(monitor)), cv2.COLOR_RGBA2RGB)
        i = 0
        while (i < int(stopClicks)):
            img = cv2.cvtColor(np.array(sct.grab(monitor)), cv2.COLOR_RGBA2RGB)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            res = cv2.matchTemplate(gray, target, cv2.TM_CCOEFF)
            a, b, min_loc, max_loc = cv2.minMaxLoc(res)
            (startX, startY) = (int(max_loc[0]), int(max_loc[1]))
            mouse.move(startX + 50 + x, startY + 50 + y)
            mouse.click()
            time.sleep(0.01)
            i += 1

    input("Press enter to exit...")