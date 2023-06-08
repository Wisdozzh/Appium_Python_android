
# coding=utf-8
import unittest
from appium import webdriver
import time
import os

from appium.webdriver.extensions.android.nativekey import AndroidKey
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
            'appPackage': 'com.honda.vspAppAndroid',
            'appActivity': 'com.nsr.module_usercenter.ui.start.StartActivity'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', calculator_desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_calculator(self):
        # real device
        # 同意隐私声明
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="同意"]').click()
        time.sleep(2)
        # 跳过介绍页面
        # self.driver.find_element(By.ID, "com.honda.vspAppAndroid:id/jump").click()
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="跳过"]').click()
        # self.driver.find_element(By.XPATH, "com.honda.vspAppAndroid:id/jump").click()
        time.sleep(2)

        # 登录页操作
        # 选择密码登录
        self.driver.find_element(By.ID, "com.honda.vspAppAndroid:id/tv_account_login").click()
        time.sleep(1)
        # 因为有记住密码 会弹出一个弹窗 点击返回按键 把那个弹窗关闭
        self.driver.press_keycode(AndroidKey.BACK)
        time.sleep(1)
        # 手机号、密码
        self.driver.find_element(By.ID, "com.honda.vspAppAndroid:id/et_phone").click()
        self.driver.press_keycode(AndroidKey.BACK)
        self.driver.find_element(By.ID, "com.honda.vspAppAndroid:id/et_phone").send_keys("15840291473")
        time.sleep(1)
        self.driver.find_element(By.ID, "com.honda.vspAppAndroid:id/et_password").click()
        self.driver.press_keycode(AndroidKey.BACK)
        self.driver.find_element(By.ID, "com.honda.vspAppAndroid:id/et_password").send_keys("qwer1234")
        time.sleep(1)
        # 点击 我已阅读并同意
        self.driver.find_element(By.ID, "com.honda.vspAppAndroid:id/checkbox").click()
        time.sleep(1)
        # 点击登录按钮
        self.driver.find_element(By.ID, "com.honda.vspAppAndroid:id/bt_login").click()
        time.sleep(5)

        # self.assertEqual(self.driver.find_element(By.ID, "com.honda.onesdk.hondaonesdk:id/tv_cabin_help").text, "什么是“座舱控制”>")

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