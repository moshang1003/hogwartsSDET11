from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTry():
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://home.testing-studio.com/')
        self.driver.set_window_size(1280,680)
        self.driver.implicitly_wait(5)
        self.wait=WebDriverWait(self.driver,10)

    def test_try(self):
        element=(By.CSS_SELECTOR,'.category-drop')
        self.wait.until(expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        locat = (By.CSS_SELECTOR, '.select-kit-body .filter-input')
        self.wait.until(expected_conditions.element_to_be_clickable(locat))
        self.driver.find_element(*locat).click()
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="搜索……"]').send_keys("教务处")
        # self.driver.find_element(By.CSS_SELECTOR, '[placeholder="搜索……"]').send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院教务处"]').click()
        self.driver.find_element(By.LINK_TEXT, "python自动化测试训练营「1期」课程表").click()

    def teardown_method(self):
        sleep(2)
        self.driver.quit()


