from selenium.webdriver.common.by import By



class Locators:
    USER_NAME = (By.CSS_SELECTOR,"#user-name")
    PASSWORD = (By.CSS_SELECTOR,"#password")
    LOGIN_BTN = (By.CSS_SELECTOR,"#login-button")


    """Main page Locator"""

    ADD_TO_CART = (By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack")
    CART_BTN = (By.CSS_SELECTOR,".shopping_cart_link")

    """Checount Page"""
    CHECKOUNT = (By.CSS_SELECTOR, "#checkout")

    """YOUR INFO"""

    FIRST_NAME =(By.CSS_SELECTOR,"#first-name")
    LASCT_NAEM =(By.CSS_SELECTOR,"#last-name")
    ZIP_CODE =(By.CSS_SELECTOR,"#postal-code")
    COUNTINE_BTN = (By.CSS_SELECTOR,"#continue")


    """FINISH PAGE"""
    FINISH_BTN =(By.CSS_SELECTOR,"#finish")


    """ASSERT WORLD"""
    PRODUCT_WORLD =(By.CSS_SELECTOR,".title")





    """COME BACK"""
    BACK_BTN =(By.CSS_SELECTOR,"#back-to-products")


