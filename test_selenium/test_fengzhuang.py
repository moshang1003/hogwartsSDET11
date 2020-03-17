from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestFengzhuang():
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://testerhome.com/')
        self.driver.set_window_size(1280, 680)
        self.driver.implicitly_wait(5)

    def wait(self,timeout,method):
        WebDriverWait(self.driver,timeout).until(method)
        #封装等待的写法

    def test_fengzhuag(self):
        element = (By.CSS_SELECTOR, '[title="MTSC2020 中国互联网测试开发大会议题征集"]')
        self.wait(10, expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()

    def teardown_method(self):
        sleep(3)
        self.driver.quit()
