from selenium import webdriver
from screeninfo import get_monitors
from selenium.webdriver.common.by import By

def typingTest():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('log-level=3')
    
    mainMonitor = get_monitors()[0]
    monitorWidth = mainMonitor.width
    monitorHeight = mainMonitor.height
    
    browser = webdriver.Chrome(options=options)
    browser.set_window_position(monitorWidth/2, 0)
    browser.set_window_size(monitorWidth/2, monitorHeight-30)
    
    url = "https://humanbenchmark.com/tests/typing"
    browser.get(url)
    
    input('Ready to start? ')
    
    text = browser.find_element(By.XPATH, './/span[@class = "incomplete current"]').text
    
    for letter in browser.find_elements(By.XPATH, './/span[@class = "incomplete"]'):
        if letter.text == "":
            text = text + " "
        else:
            text = text + letter.text
    
    browser.find_element(By.XPATH, './/div[@class = "letters notranslate"]').send_keys(text)
    
    input("Press enter to exit...")