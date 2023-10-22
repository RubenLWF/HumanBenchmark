from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import cv2
import mss.tools
import numpy as np

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('log-level=3')

browser = webdriver.Chrome(options=options)
browser.set_window_position(1270, 0)
browser.set_window_size(1300, 1050)
window = browser.get_window_position()

img = cv2.imread('target.png', 0)

url = "https://humanbenchmark.com/tests/aim"
browser.get(url)

print('Ready to start?')
startWait = input()

e = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[2]')
location = e.location
size = e.size
w, h = size['width'], size['height']
x = window['x'] + location['x']
y = window['y'] + location['y'] + 131

target = cv2.imread("target2.jpg", 1)
target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
target = cv2.Canny(target, 50,200)

with mss.mss() as sct:
    # The screen part to capture
    monitor = {"top": y, "left": x, "width": w, "height": h}
    output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

    i = 0

    while i <= 30:
        img = np.array(sct.grab(monitor))
        gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
        #edged = cv2.Canny(gray, 50, 200)
        res = cv2.matchTemplate(gray, target, cv2.TM_CCOEFF)
        a, b, min_loc, max_loc = cv2.minMaxLoc(res)
        (startX, startY) = (int(max_loc[0]), int(max_loc[1]))
        pyautogui.click(startX + 50 + x, startY + 50 + y)
        i += 1

#i = 0
#while i <= 30:
#    target = pyautogui.locateOnScreen('target.png', region = (x,y,w,h), grayscale = True, confidence = 0.3)
#    target_center = pyautogui.center(target)
#    pyautogui.click(target_center[0], target_center[1])