from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLianshou():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://testerhome.com/')
        self.driver.set_window_size(1280,680)
        self.driver.implicitly_wait(5)
        #隐性等待
        self.wait=WebDriverWait(self.driver,10)
        #显性等待

    def test_lianshou(self):
        element=(By.CSS_SELECTOR,'[title="MTSC2020 中国互联网测试开发大会议题征集"]')
        self.wait.until(expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        self.driver.find_element(By.CSS_SELECTOR,'.toc-container span').click()
        self.driver.find_element(By.LINK_TEXT,'征集议题范围').click()

    def teardown_method(self):
        sleep(3)
        #死等
        self.driver.quit()





