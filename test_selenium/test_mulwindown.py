from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestMulwindown():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def wait(self, timeout, method):
        WebDriverWait(self.driver, timeout).until(method)
        # 封装等待的写法

    def test_multiwindown(self):
        self.driver.get('https://testerhome.com/topics/21805')
        self.driver.find_element(By.PARTIAL_LINK_TEXT,'第六届中国互联网测试开发大会').click()
        #点击第六届中国互联网测试开发大会链接
        print(self.driver.window_handles)
        # 打印查看是否有多窗口
        self.wait(10, lambda x:len(self.driver.window_handles)>1)
        #10S内每隔0.5秒判断window_handles是否>1
        self.driver.switch_to.window(self.driver.window_handles[1])
        #切到第二个窗口
        self.driver.find_element(By.LINK_TEXT,'演讲申请').click()
        #点击演讲申请链接

    def teardown_method(self):
        sleep(3)
        self.driver.quit()


# 多浏览器函数写法
#     def setup_method(self):
#         browser=os.getenv("browser","").lower()
#
#         if browser =="headless":
#             self.driver = webdriver.PhantomJS()
#         elif browser=="firedox":
#             self.driver=webdriver.Firefox()
#         else:
#             self.driver=webdriver.Chrome()
#         self.driver.get('https://testerhome.com/topics/21805')
#
#
#         可以在ternimal用命令执行：broswer=firefox pytest 路径/包名
#         如：broswer=firefox pytest test_selunium/test_mulwindown.py

#self.driver=webdriver.Chrome(options={}) 把option的值赋给chrome,当chrome启动时追加进去
#使用headless模式运行自动化
# options=webdriver.ChromeOptions()
# options.add_argument("--headless")
# self.driver =webdriver.Chrome(options=options)
