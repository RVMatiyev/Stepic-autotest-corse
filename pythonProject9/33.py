from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome(executable_path="O:\chromedriver_win32\chromedriver.exe")
    browser.get(link)


    x_element = browser.find_element_by_id("num1")
    x = x_element.text


    x2_element = browser.find_element_by_id("num2")
    x2 = x2_element.text

    y= (int(x)+int(x2))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(y))

    button = browser.find_element_by_xpath("//button").click()
finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()




