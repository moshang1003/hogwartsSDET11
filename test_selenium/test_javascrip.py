# 执行Javascript脚本
#Javascript 是浏览器的语言，用来解决H5的一些行为；（整个网页由html组成）
# Javascript 决定了网页的动态效果，点击效果，展示效果。
import self
from selenium import webdriver


class TestJavaScript():

    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://testerhome.com')
        self.driver.implicitly_wait(5)

    def test_js(self):
        # todo: 专项测试的时候会讲如何获取性能
        for code in [
            "return document.title",
            'return document.querySelector(".active").className',
            'return JSON.(performance.timing)'
        ]:
            result = self.driver.execute_script(code)
            print(result)

    def teardown_method(self):
        sleep(3)
        self.driver.quit()
# return JSON.stringify(performance.timing) 返回关键性能数据
#"return document.title",返回title
#'return document.querySelector(".active").className', 返回document.querySelector(".active").className
