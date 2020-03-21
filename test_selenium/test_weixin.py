# 此用例使用已登录的页面才能执行，免cookie;打开chrome安装页面，powershelll命令：.\chrome.exe --remote-debugging-port=9222
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWeixin():
    def setup_method(self):
        chromeOptions = Options()
        # 定义option，复用已经打开浏览器方法，可免cookie
        chromeOptions.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # 添加debuggerAddress参数,指定本地路径和端口
        self.driver = webdriver.Chrome(options=chromeOptions)
        # 声明driver并添加options
        self.driver.set
        self.driver.implicitly_wait(5)
        # 隐式等待，无论写在哪个地方都对全局find_element和find_elements有效，无论触发那个操作都执行此等待
        self.wait = WebDriverWait(self.driver, 10)

    def wait_element(self, x):
        size = len(self.driver.find_elements(By.ID, 'username'))
        # self.driver.find_elements(By.ID,'username') 判断username是否可找到
        if size < 1:
            self.driver.find_element(By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member').click()
        return size >= 1
        # 判断username是否可点击，不可点击的话循环点击添加成员按钮

    def test_weixin(self):
        self.driver.find_element(By.ID, 'menu_contacts').click()
        # 点击通讯录
        WebDriverWait(self.driver, 10).until(self.wait_element)
        # while True:
        #     self.wait_element()
        # self.driver.find_element(By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member').click()
        # 添加成员
        self.driver.find_element(By.ID, 'username').send_keys("陌上")
        # 添加姓名
        self.driver.find_element(By.ID, 'memberAdd_english_name').send_keys("陌路")
        # 添加别名
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys("123")
        # 添加账号
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys("13250271009")
        # 添加手机号
        self.driver.find_element(By.ID, 'memberAdd_title').send_keys("职务")
        # 添加职务
        self.driver.find_element(By.LINK_TEXT, "保存").click()
        # 保存
        aa='保存成功'
        assert aa in "保存成功"
        element = (By.CSS_SELECTOR, '[id="member_list"] tr:nth-child(1) input')
        self.wait.until(expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        # 另一个写法
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[id="member_list"] tr:nth-child(1) input')))
        # self.driver.find_element(By.CSS_SELECTOR, '[id="member_list"] tr:nth-child(1) input').click()
        # 勾选
        self.driver.find_element(By.LINK_TEXT, "删除").click()
        # 删除
        self.driver.find_element(By.LINK_TEXT, "确认").click()
        bb="删除成功"
        assert bb in "删除成功"

    def tesrdown_method(self):
        sleep(2)
        self.driver.quit()
