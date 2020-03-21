# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# from test_selenium.page.index import Index
#
#
# class TestIndex():
#     def setup(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(3)
#         self.driver.get('https://work.weixin.qq.com/')
#         self.driver.maximize_window()
#
#     def test_register(self):
#         # self.driver=webdriver.Chrome()
#         # self.driver.implicitly_wait(3)
#         # self.driver.get('https://work.weixin.qq.com/')
#         # self.driver.find_element(By.LINK_TEXT,"立即注册").click()
#         # self.driver.find_element(By.ID,"corp_name").send_keys("霍格沃兹测试学院")
#         # self.driver.find_element(By.ID, "manager_name").send_keys("管理员")
#         # self.driver.find_element(By.ID, "iagree").click()
#         # self.driver.find_element(By.ID, "submit_btn").click()
#         index=Index (self.driver)
#         #创建index,要求传driver
#         index.goto_register().register("霍格沃兹测试学院")
#         #链式跳转

# 第二种写法
# from test_selenium.page.index import Index
#
#
# class TestIndex():
#     def setup(self):
#         self.index=Index()
#
#     def test_register(self):
#         self.index.goto_register().register("霍格沃兹测试学院")
# 链式跳转

# 第三种写法（把重复代码init封装起来，此页面不涉及）

from test_selenium.page.index import Index


class TestIndex():
    def setup(self):
        self.index = Index()
        # 初始化

    def test_register(self):
        self.index.goto_register().register("霍格沃兹测试学院")
        # 执行步骤

    def test_login(self):
        register_page = self.index.goto_login().goto_register().register("测吧(北京)科技有限公司")
        print(register_page.get_error_message())
        # 打印register_page.get_error_message()内容
        print("|".join(register_page.get_error_message()))
        # 打印"|".join( register_page.get_error_message()输出内容
        assert "请选择" in "|".join(register_page.get_error_message())
        # 断言，判断“请选择”是否在register_page.get_error_message()中 ；“|”连接符号

    def teardown(self):
        self.index.close()
        # 关闭页面
