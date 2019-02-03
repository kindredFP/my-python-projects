from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class MyUnitTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('..//resourceFiles/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.close()

    def test1(self):
        browser = self.browser
        browser.get("http://www.google.ca")

        self.assertIn("Google", browser.title)
        elem = browser.find_element_by_name("q")
        elem.send_keys("TestingBot")
        elem.submit()

    def test2(self):
        browser = self.browser
        browser.get("http://www.yahoo.ca")

        self.assertIn("Yahoo",browser.title)
        elem = self.browser.find_element_by_name("p")
        elem.send_keys("anotherTest")
        elem.submit()


    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()