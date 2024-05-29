from selenium import webdriver
from screeninfo import get_monitors
from selenium.webdriver.common.by import By

def chimpTest():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('log-level=3')

    mainMonitor = get_monitors()[0]
    monitorWidth = mainMonitor.width
    monitorHeight = mainMonitor.height

    browser = webdriver.Chrome(options=options)
    browser.set_window_position(monitorWidth/2, 0)
    browser.set_window_size(monitorWidth/2, monitorHeight-30)

    url = "https://humanbenchmark.com/tests/chimp"
    browser.get(url)
    
    stopScore = input('What score do you want to go to? ')
    
    if (int(stopScore) > 37):
        stopScore = 37
        
    input('Ready to start? ')
    
    
    i = 0
    while (i < int(stopScore)):
        if (i == 0):
            browser.find_element(By.XPATH, '//button[text()="Start Test"]').click()
        else:
            browser.find_element(By.XPATH, '//button[text()="Continue"]').click()
    
        j = 1
        while (j <= i + 4):
            browser.find_element(By.XPATH, "//div[@data-cellnumber='{num}']".format(num = str(j))).click()
            j += 1
        i += 1
    
    input("Press enter to exit...")