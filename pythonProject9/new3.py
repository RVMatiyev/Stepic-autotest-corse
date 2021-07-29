from selenium import webdriver
import time

link = "http://suninjuly.github.io/wait2.html"

try:
    browser = webdriver.Chrome(executable_path="O:\chromedriver_win32\chromedriver.exe")
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get(link)

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:

    time.sleep(5)

    browser.quit()
