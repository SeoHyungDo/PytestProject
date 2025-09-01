import pytest
import time
from selenium.webdriver.common.by import By
from utility.passclass import passclass


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
        expected_text = "오픈마켓\n여행·티켓\n로켓배송\n제휴마케팅\n로켓그로스"
        self.driver.find_element(By.XPATH, '//*[@id="subscribeHeader"]/li[2]/a').click()
        apply_store_select_box = self.driver.find_elements(By.XPATH,'//*[@id="subscribeHeader"]/li[2]/p')
        for select_box_text in apply_store_select_box:
            apply_store_select_box_text = select_box_text.text
        assert apply_store_select_box_text == expected_text

    def test_login_button(self):
        login_button = self.driver.find_element(By.XPATH, '//*[@id="wa-top-bar"]/div/menu[1]/li[4]/a')
        login_button_text = login_button.text
        assert login_button_text == "로그인"

    def test_customer_join(self):
        join_button = self.driver.find_element(By.XPATH, '//*[@id="wa-top-bar"]/div/menu[1]/li[3]/a')
        join_button_text = join_button.text
        assert join_button_text == "회원가입"

    def test_customer_service_center(self):
        customer_service_center = self.driver.find_element(By.XPATH, '//*[@id="wa-top-bar"]/div/menu[1]/li[2]/a')
        customer_service_center_text = customer_service_center.text
        assert customer_service_center_text == "고객센터"

    def test_seller_join(self):
        seller_join_button = self.driver.find_element(By.XPATH, '//*[@id="wa-top-bar"]/div/menu[1]/li[1]/a')
        seller_join_button_text = seller_join_button.text
        assert seller_join_button_text == "판매자 가입"