from appium import webdriver


class AppStart:
    # 声明driver对象
    driver: webdriver = None

    # 使用classmethod方法，可以直接调用类中的属性和函数
    @classmethod
    def start(cls):
        caps = {
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
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        cls.driver.implicitly_wait(20)
        return LoginPage(cls.driver)

    # 退出
    @classmethod
    def quit(cls):
        cls.driver.quit()
