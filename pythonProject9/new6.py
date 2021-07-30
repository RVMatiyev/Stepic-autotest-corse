from selenium import webdriver
import time
import unittest


link1 = "http://suninjuly.github.io/registration2.html"
link2 = "http://suninjuly.github.io/registration1.html"


browser = webdriver.Chrome(executable_path="O:\chromedriver_win32\chromedriver.exe")
browser.get(link1)

input1 = browser.find_element_by_css_selector("div > input")
input1.send_keys("Roman")

input2 = browser.find_element_by_css_selector("div:nth-child(2) .second")
input2.send_keys("Romanow")

input3 = browser.find_element_by_css_selector("div:nth-child(3) .third")
input3.send_keys("Roma@mail.ru")

button = browser.find_element_by_xpath('//button')
button.click()

time.sleep(1)

welcome_text_elt = browser.find_element_by_tag_name("h1")

welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text


class Testlinks(unittest.TestCase):
    def test_first(self):
        self.assertEqual(first(link1), "Congratulations! You have successfully registered!", "OSHIBKO")

    def test_second(self):
        self.assertEqual(second(link2), "Congratulations! You have successfully registered!", "OSHIBKO")

if __name__ == "__main__":
    unittest.main()


