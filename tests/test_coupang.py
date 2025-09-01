import pytest
import time
from selenium.webdriver.common.by import By

from utility.passclass import passclass


# @pytest.mark.usefixtures("setup")

class Test_CoupangTest(passclass) :

    def test_favorite_name(self) :
        favorite_name = self.driver.find_element(By.XPATH,'//*[@id="wa-bookmark"]')
        favorite_name_text = favorite_name.text
        assert favorite_name_text == "즐겨찾기"

    def test_apply_store(self) :
        apply_store = self.driver.find_element(By.XPATH,'//*[@id="subscribeHeader"]/li[2]/a')
        apply_store_text = apply_store.text
        assert apply_store_text == "입점신청"

