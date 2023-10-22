from selenium import webdriver
from selenium.webdriver.common.by import By
import mouse
import mss.tools
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('log-level=3')

browser = webdriver.Chrome(options=options)
browser.set_window_position(1270, 0)
browser.set_window_size(1300, 1050)
window = browser.get_window_position()

url = "https://humanbenchmark.com/tests/reactiontime"
browser.get(url)

print('Ready to start?')
startWait = input()

div = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div')
location = div.location
size = div.size
x = window['x'] + location['x']
y = window['y'] + location['y'] + 131
monitor = {"top": y + 10, "left": x + 10, "width": 1, "height": 1}

i = 0
while i <= 4:
    if (mss.mss().grab(monitor).pixel(0,0) == (75,218,106)):
        mouse.click()
        time.sleep(0.5)
        mouse.click()
        i += 1