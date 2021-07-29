from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome(executable_path="O:\chromedriver_win32\chromedriver.exe")
    browser.get(link)

    Input1 = browser.find_element_by_css_selector("[name='firstname']")
    Input1.send_keys("Roman")

    Input2 = browser.find_element_by_name("lastname")
    Input2.send_keys("Matiev")

    Input3 = browser.find_element_by_name("email")
    Input3.send_keys("roma@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "text.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_css_selector("[accept='.txt']")
    element.send_keys (file_path)

    button = browser.find_element_by_tag_name("button").click()


finally:

    time.sleep(10)

    browser.quit()



