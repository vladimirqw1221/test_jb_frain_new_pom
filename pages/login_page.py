import time

import allure

from base_pages.base_page import Base
from generators.generator import generated_person
from pages.locators import Locators


class Login(Base):
    locator = Locators()




    def page_in_login(self):
        with allure.step('page_in_login'):
            self.element_is_visubel(self.locator.USER_NAME).send_keys("standard_user")
            self.element_is_visubel(self.locator.PASSWORD).send_keys("secret_sauce")
            self.element_is_clicable(self.locator.LOGIN_BTN).click()
            time.sleep(3)


    def page_in_main(self):
        ae = self.element_is_visubel(self.locator.PRODUCT_WORLD)
        self.get_cerrent_url(),"error"
        self.element_is_visubel(self.locator.PRODUCT_WORLD)
        self.cheh_assert_world(ae,"PRODUCTS") , " ERORR ASSERT WORLD "
        self.element_is_clicable(self.locator.ADD_TO_CART).click()
        self.element_is_clicable(self.locator.CART_BTN).click()
        time.sleep(3)


    def cart_on_page(self):
        self.get_cerrent_url()
        self.element_is_clicable(self.locator.CHECKOUNT).click()
        time.sleep(3)


    def info_page_pres(self):
        person_info = next(generated_person())
        first_name = person_info.fist_name
        last_name = person_info.last_name
        zip_code = person_info.zip_code
        self.get_cerrent_url()
        self.element_is_visubel(self.locator.FIRST_NAME).send_keys(first_name)
        self.element_is_visubel(self.locator.LASCT_NAEM).send_keys(last_name)
        self.element_is_visubel(self.locator.ZIP_CODE).send_keys(zip_code)
        self.element_is_clicable(self.locator.COUNTINE_BTN).click()
        time.sleep(4)


    def finish_page(self):
        self.get_cerrent_url()
        self.element_is_clicable(self.locator.FINISH_BTN).click()

    def come_back(self):
        self.get_cerrent_url()
        self.element_is_clicable(self.locator.BACK_BTN).click()
        ae = self.element_is_visubel(self.locator.PRODUCT_WORLD)
        self.cheh_assert_world(ae, "PRODUCTS"), " ERORR ASSERT WORLD "



