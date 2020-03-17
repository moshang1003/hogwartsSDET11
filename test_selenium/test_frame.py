from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestFengzhuang():
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://testerhome.com/topics/21495')
        self.driver.set_window_size(1280, 680)
        self.driver.implicitly_wait(5)

    def wait(self,timeout,method):
        WebDriverWait(self.driver,timeout).until(method)
        #封装等待的写法

    def test_fengzhuag(self):
        element = (By.CSS_SELECTOR, '.published-form_submit')

        self.driver.switch_to.frame(0)
        #切换到特定的frame（可以用名字、序号和id定位）
        # driver.switch_to.frame('frame_name')
        # driver.switch_to.frame(1)
        # driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
        #self._driver.execute(Command.SWITCH_TO_FRAME, {'id': frame_reference})
        self.wait(10, expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()

        # print(self.driver.window_handles)
        # 打印查看是否有多窗口




    def teardown_method(self):
        sleep(3)
        self.driver.quit()
