import pytest
import time
from selenium.webdriver.common.by import By

from utility.passclass import passclass_tw


# @pytest.mark.usefixtures("setup")
class Test_CoupangTest(passclass_tw) :

    def test_favorite_name_tw(self) :
        favorite_name = self.driver.find_element(By.XPATH,'//*[@id="wa-bookmark"]')
        favorite_name_text = favorite_name.text
        assert favorite_name_text == "加到我的最愛"

    def test_login_button_tw(self):
        login_button = self.driver.find_element(By.XPATH, '//*[@id="wa-top-bar"]/div/menu[1]/li[2]/a')
        login_button_text = login_button.text
        assert login_button_text == "登入"