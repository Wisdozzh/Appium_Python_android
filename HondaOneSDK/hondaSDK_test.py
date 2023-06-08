
# coding=utf-8
import unittest
from appium import webdriver
import time
import os

from selenium.webdriver.common.by import By


class AndroidSimpleTest(unittest.TestCase):
    def setUp(self):
        calculator_desired_caps = {
            'platformName': 'Android',
            'platformVersion': '12.0',
            # emulator
            # 'deviceName': 'emulator-5554',
            # 'appPackage': 'com.android.calculator2',
            # 'appActivity': 'com.android.calculator2.Calculator'
            # real device
            'deviceName': 'CTV0221420004654',
            'appPackage': 'com.honda.onesdk.hondaonesdk',
            'appActivity': 'com.honda.onesdk.hondaonesdk.MainActivity'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', calculator_desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_calculator(self):
        # real device
        self.driver.find_element(By.ID, "com.honda.onesdk.hondaonesdk:id/button").click()
        time.sleep(5)
        self.assertEqual(self.driver.find_element(By.ID, "com.honda.onesdk.hondaonesdk:id/tv_cabin_help").text, "什么是“座舱控制”>")
        time.sleep(5)

        # ************
        # emulator
        # self.driver.find_element_by_id("digit_5").click()
        # self.driver.find_element_by_accessibility_id("plus").click()
        # self.driver.find_element_by_id("digit_6").click()
        # self.driver.find_element_by_accessibility_id("equals").click()
        # self.assertEqual(self.driver.find_element_by_id("result").text, "11")

    @unittest.skip("skip")
    def test_something(self):
        pass


if __name__ == '__main__':
    unittest.main()