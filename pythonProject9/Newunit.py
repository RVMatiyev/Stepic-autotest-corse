import unittest
from selenium import webdriver
import time


link1 = "http://suninjuly.github.io/registration1.html"

link2 = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome(executable_path="O:\chromedriver_win32\chromedriver.exe")

class TestLink(unittest.TestCase):
    def test_link1(self):

        browser.get(link1)

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

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "failed")

    def test_link2(self):

        browser.get(link2)

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

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "failed")

if __name__ == '__main__':
    unittest.main()
