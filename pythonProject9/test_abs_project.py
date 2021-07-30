#def test_abs1():
   # assert abs(-42) == 42, "Should be absolute value of a number"

#def test_abs2():
 #   assert abs(-42) == -42, "Should be absolute value of a number"

#if __name__ == "__main__":
 #   test_abs1()
  #  test_abs2()
   # print("Everything passed")

import unittest
from task new import Input1
    import time

    link = "http://suninjuly.github.io/registration2.html"

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()

class test_class_name(unittest.TestCase):
    def test_class_name1(self):
    self.assertEqual


   # try:
        browser = webdriver.Chrome(executable_path="O:\chromedriver_win32\chromedriver.exe")
        browser.get("http://suninjuly.github.io/registration2.html")

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




    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()