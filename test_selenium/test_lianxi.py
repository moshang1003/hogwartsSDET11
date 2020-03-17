
#进入testerhome，访问MTSC2020置顶帖，点击目录，点击议题征集范围

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testlianxi():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        self.driver.set_window_size(1280, 680)
        self.driver.implicitly_wait(5)
        self.wait=WebDriverWait(self.driver, 10)

    def test_testlianxi(self):
        element=(By.LINK_TEXT,"MTSC2020 中国互联网测试开发大会议题征集")
        self.wait.until(expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        #self.driver.find_element(By.LINK_TEXT,"MTSC2020 中国互联网测试开发大会议题征集").click()
        self.driver.find_element(By.CSS_SELECTOR, '.caret').click()
        self.driver.find_element(By.LINK_TEXT,"征集议题范围").click()

    def teardown_method(self):
        self.driver.quit()
