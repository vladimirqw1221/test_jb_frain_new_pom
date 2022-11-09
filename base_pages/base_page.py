from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

class Base:
    def __init__(self , driver , url):
        self.driver = driver
        self.url = url

    """Open page in browser"""

    def open_page(self):
        self.driver.get(self.url)


    """Element command"""

    def element_is_visubel(self, locator , timeout=5):
        return wait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visubel(self, locator , timeout=5):
        return wait(self.driver,timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_presence(self, locator , timeout=5):
        return wait(self.driver,timeout).until(EC.presence_of_element_located(locator))

    def element_are_presence(self, locator , timeout=5):
        return wait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_clicable(self, locator , timeout=5):
        return wait(self.driver,timeout).until(EC.element_to_be_clickable(locator))

    def swiching_to_frame(self,timeout=5):
        return wait(self.driver,timeout).until(EC.frame_to_be_available_and_switch_to_it(0))


    """SCRIT JS"""
    def element_to_scroll(self,element):
        return self.driver.execute_script("argument[0].scrollIntoView;", element)


    """CURRENT URL"""
    def get_cerrent_url(self):
        get_url = self.driver.current_url
        print("Current url : " + get_url)


    """ASSERT WORLD """
    def cheh_assert_world(self, world , result):
        value_world = world.text
        assert value_world == result
        print(" ASEERT TEST PASS")




