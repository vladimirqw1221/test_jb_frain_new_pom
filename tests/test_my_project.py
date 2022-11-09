import time

from pages.login_page import Login


class TestElement:
    class TestCommant:
        def test_on_project(self ,driver):
            test_page = Login(driver, "https://www.saucedemo.com/")
            test_page.open_page()
            time.sleep(5)
            test_page.page_in_login()
            test_page.page_in_main() , "add to cart"
            test_page.cart_on_page()
            test_page.info_page_pres()
            test_page.finish_page(), " EROOR FINISH"
            test_page.come_back(), " EROOR BACK"
