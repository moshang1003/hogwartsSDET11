from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.test_mulwindown import TestMulwindown


class TestBrower(TestMulwindown):
    #继承于TestMulwindown
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://testerhome.com/topics/21805')
        self.driver.implicitly_wait(5)



