# from selenium import webdriver
#
#
# class Basepage():
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

#第二种写法 把url更换为base_url(此url在每个类定义)
from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class Basepage():
    def __init__(self,driver: WebDriver=None):
        if driver==None:
            self._driver = webdriver.Chrome()
            #选中driver--右键--refactor-rename,编辑为_driver,可使全部相关的driver改为_driver(隐藏起来)
            self._driver.implicitly_wait(3)
            self._driver.get(self._base_url)
            #使用下划线_base_url则设置为隐私
            self._driver.maximize_window()
            #如果driver为空，页面初始化创建driver；index页面使用此方法
        else:
            self._driver=driver
            #如果driver不为空，self.driver=driver,直接复用已有的driver;login和register等页面需要用此方法

    def close(self):
        sleep(1)
        self._driver.quit()

