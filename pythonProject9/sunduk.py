from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome(executable_path="O:\chromedriver_win32\chromedriver.exe")
    browser.get("http://suninjuly.github.io/get_attribute.html")

    x_element = browser.find_element_by_xpath("//h2/img")
    x_valuex = x_element.get_attribute("valuex")
    x = x_valuex
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_xpath("//input[3]")
    option2.click()

    button = browser.find_element_by_xpath('//button')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()