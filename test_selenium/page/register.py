# from selenium.webdriver.common.by import By
#
#
# class Register():
#     def __init__(self,driver):
#         self.driver=driver
#     #driver初始化，从外面传入
#
#     def register(self,corpname):
#         self.driver.find_element(By.ID, "corp_name").send_keys(corpname)
#         self.driver.find_element(By.ID, "manager_name").send_keys("管理员")
#         self.driver.find_element(By.ID, "iagree").click()
#         self.driver.find_element(By.ID, "submit_btn").click()

#第二种写法
# from selenium.webdriver.common.by import By
#
# class Register():
#     def __init__(self,driver):
#         self.driver=driver
#     #driver初始化，从外面传入
#
#     def register(self,corpname):
#         self.driver.find_element(By.ID, "corp_name").send_keys(corpname)
#         self.driver.find_element(By.ID, "manager_name").send_keys("管理员")
#         self.driver.find_element(By.ID, "iagree").click()
#         self.driver.find_element(By.ID, "submit_btn").click()

#第三种写法（把重复代码init封装起来）
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

from test_selenium.page.base_page import Basepage


class Register(Basepage):

    def register(self,corpname):
        self._driver.find_element(By.ID, "corp_name").send_keys(corpname)
        self._driver.find_element(By.ID, "manager_name").send_keys("管理员")
        self._driver.find_element(By.ID, "iagree").click()
        self._driver.find_element(By.ID, "submit_btn").click()
        return self

    def get_error_message(self):
        result=[]
        for element in self._driver.find_elements(By.CSS_SELECTOR,'.js_error_msg'):
            result.append(element.text)
        return result
    #查找所有js_error_msg定位
