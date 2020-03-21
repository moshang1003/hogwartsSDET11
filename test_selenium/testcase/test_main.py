from test_selenium.page.main import Main


class TestMain():
    def test_add_member(self):
        main=Main()
        main.add_menber().add_menber("xx")
        #链式调用,跳转多个页面，使多个页面链接起来进行测试
        main.import_user().get_message()
        #查看返回信息
