from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome(executable_path="O:\chromedriver_win32\chromedriver.exe")
    browser.get("http://suninjuly.github.io/find_xpath_form")
    input1 = browser.find_element_by_class_name("form-control")
    input1.send_keys("Roman")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Romanow")
    input3 = browser.find_element_by_name("firstname")
    input3.send_keys("Perm")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath('/html/body/div/form/div[6]/button[@type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла