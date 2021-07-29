from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome(executable_path="O:\chromedriver_win32\chromedriver.exe")
    browser.get(link)

    x_element = browser.find_element_by_xpath("//label/span[2]")
    x = x_element.text
    y = calc(x)

    #Скрипт для скрола страницы
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']").click()

    option2 = browser.find_element_by_css_selector("[for='robotsRule']").click()

finally:

    time.sleep(10)
    browser.quit()




