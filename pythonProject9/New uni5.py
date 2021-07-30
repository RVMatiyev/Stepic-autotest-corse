import unittest
from selenium import webdriver

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome(executable_path="O:\chromedriver_win32\chromedriver.exe")
        browser.get("http://suninjuly.github.io/registration2.html")

class test_class_name(unittest.TestCase):

    def test_input1(self):
        input1 = browser.find_element_by_css_selector("div > input")
        input1.send_keys("Roman")
        self.assertEqual(input1.get_attribute('placeholder'), "not such input")

    def test_input2(self):
        input2 = browser.find_element_by_css_selector("div:nth-child(2) .second")
        input2.send_keys("Romanow")
        self.assertEqual(input2.get_attribute('placeholder'), "not such element")

    def test_input3(self):
        input3 = browser.find_element_by_css_selector("div:nth-child(3) .third")
        input3.send_keys("Roma@mail.ru")
        self.assertEqual(input3.get_attribute('placeholder'), "not such element")

    def test_button(self):
        button = browser.find_element_by_xpath('//button')
        button.click()
        self.assertEqual(button.text("Congratulations! You have successfully registered!"), "button click error")


if __name__ == '__main__':
    unittest.main()
