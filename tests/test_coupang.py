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

    def test_apply_store_selectbox(self):
        expected_texts = "오픈마켓\n여행·티켓\n로켓배송\n제휴마케팅\n로켓그로스"
        self.driver.find_element(By.XPATH, '//*[@id="subscribeHeader"]/li[2]/a').click()
        apply_store_select_box = self.driver.find_elements(By.XPATH,'//*[@id="subscribeHeader"]/li[2]/p')
        for select_box_text in apply_store_select_box:
            apply_store_select_box_text = select_box_text.text
        assert apply_store_select_box_text == expected_texts