from selenium import webdriver
import time


link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome(executable_path="O:\chromedriver_win32\chromedriver.exe")
    browser.get("http://suninjuly.github.io/registration2.html")

    input1 = browser.find_element_by_xpath('//div[@class="first_block"] //input[@class="form-control first"]')
    input1.send_keys("Roman")

    input2 = browser.find_element_by_xpath('//div[@class="first_block"] //input[@class="form-control second"]')
    input2.send_keys("Romanow")

    input3 = browser.find_element_by_xpath('//div[@class="first_block"] //input[@class="form-control third"]')
    input3.send_keys("Roma@mail.ru")

    button = browser.find_element_by_xpath('//button')
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")

    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()