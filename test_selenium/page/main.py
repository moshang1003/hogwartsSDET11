from test_selenium.page.contact import Contact


class Main():
    def download(self):
        pass

    def import_user(self, user):
        return self
    #如果导入后停留在当前页面，则return self就可以
    #返回后用例的写法main.import_user().get_message()

    def goto_app(self):
        pass

    def goto_company(self):
        pass

    def get_message(self):
        return ["aaa","bbb"]
    #返回后用例的写法为 assert "aaa"in  main.import_user().get_message()

    def add_menber(self):
        return Contact()


