# #企业微信首页
# from selenium.webdriver.common.by import By
#
# from test_selenium.page.register import Register
#
#
# class Index():
#     def __init__(self,driver):
#         self.driver=driver
#     #driver初始化，从外面传入
#
#     def goto_register(self):
#         self.driver.find_element(By.LINK_TEXT, "立即注册").click()
#         return  Register(self.driver)

# 第二种写法
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from test_selenium.page.register import Register
#
#
# class Index():
#     def __init__(self,driver=None):
#         if driver==None:
#             self.driver = webdriver.Chrome()
#             self.driver.implicitly_wait(3)
#             self.driver.get('https://work.weixin.qq.com/')
#             self.driver.maximize_window()
#             #如果driver为空，页面初始化
#         else:
#             self.driver=driver
#             #如果driver不为空，self.driver=driver
#
#     def goto_register(self):
#         self.driver.find_element(By.LINK_TEXT, "立即注册").click()
#         return  Register(self.driver)

# 第三种写法（把重复代码init封装起来）
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# from test_selenium.page.base_page import Basepage
# from test_selenium.page.register import Register
#
#
# class Index(Basepage):
#
#     def goto_register(self):
#         self.driver.find_element(By.LINK_TEXT, "立即注册").click()
#         return  Register(self.driver)

# 第四中写法，增加base_url
from selenium.webdriver.common.by import By

from test_selenium.page.base_page import Basepage
from test_selenium.page.login import Login
from test_selenium.page.register import Register


class Index(Basepage):
    _base_url = "https://work.weixin.qq.com/"

    # 加下划线则设置为隐私，每个类自己定义url，使base_url变为公共方法
    # 立即注册跳转
    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT, "立即注册").click()
        return Register(self._driver)

    # 企业登录跳转
    def goto_login(self):
        self._driver.find_element(By.LINK_TEXT, "企业登录").click()
        return Login(self._driver)
