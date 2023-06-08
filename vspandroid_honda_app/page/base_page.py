from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    # 初始化，定义driver的类型为WebDriver
    def __int__(self, driver: WebDriver):
        self.driver = driver

    # 根据id定位
    def find_element(self, locator):
        try:
            # 单个元素定位，获取到的是单个元素的位置
            return self.driver.find_element(*locator)
        except:
            # 多个相同id元素定位，获取到的是列表，具体某个元素的位置可以使用列表查询
            return self.driver.find_elements(*locator)

    # 根据xpath定位
    def find_xpath(self, locator):
        try:
#             单个元素定位，获取到的是单个元素的位置
            return self.driver.find_element_
