from selenium.webdriver.common.by import By

from test_selenium.page.base_page import Basepage
from test_selenium.page.register import Register


class Login(Basepage):
    def scan_qrcode(self):
        pass
        #扫码
    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT, "企业注册").click()
        return Register(self._driver)
