from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome(executable_path="O:\chromedriver_win32\chromedriver.exe")
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока цена не станет равна 100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element_by_id("book")
    button.click()

    x_element = browser.find_element_by_xpath("//label/span[2]")
    x = x_element.text
    y = calc(x)

    Input = browser.find_element_by_name("text")
    Input.send_keys(y)

    button2 = browser.find_element_by_xpath("//form/div/div/button").click()

finally:

    time.sleep(15)

    browser.quit()
