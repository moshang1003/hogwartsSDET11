from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(5)
        self.wait=WebDriverWait(self.driver,10)
        # 隐式等待

    def test_hogwarts(self):
        self.driver.find_element(By.LINK_TEXT, "社团").click()
        #sleep(2)
        #todo:显式等待

        element=(By.CSS_SELECTOR, '[title="霍格沃兹测试学院(hogwarts)"]')
        self.wait.until(expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        #d最多等待10秒，直到可点击
        #self.driver.find_element(By.CSS_SELECTOR, '[title="霍格沃兹测试学院(hogwarts)"]').click()
        #self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院").click()
        #todo:隐式等待
        self.driver.find_element(By.CSS_SELECTOR, '.topic:nth-child(1) .title a').click()
        #self.driver.find_element(By.CSS_SELECTOR, ".topic-22195 .title > a").click()




    def teardown_method(self):
        sleep(3)
        self.driver.quit()
