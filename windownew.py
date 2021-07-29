from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome(executable_path="O:\chromedriver_win32\chromedriver.exe")
    browser.get(link)

    button = browser.find_element_by_tag_name("button").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_xpath("//label/span[2]")
    x = x_element.text
    y = calc(x)

    Input1 = browser.find_element_by_css_selector("[name='text']")
    Input1.send_keys(y)

    button2 = browser.find_element_by_xpath("//button").click()

finally:

    time.sleep(10)

    browser.quit()
