import pytest
import time
from selenium.webdriver.common.by import By

from utility.passclass import passclass


# @pytest.mark.usefixtures("setup")

class Test_CoupangTest(passclass) :

    def test_favorite_name(self, setup) :
        # logger = self.get_logger() #Baseclass에 선언한 로그를 불러오는 객체
        favorite_name = self.driver.find_element(By.XPATH,'//*[@id="wa-bookmark"]')
        apply_store = self.driver.find_element(By.XPATH,'//*[@id="subscribeHeader"]/li[2]/a')
        favorite_name_text = favorite_name.text
        apply_store_text = apply_store.text
        
        assert favorite_name_text == "즐겨찾기"
        assert apply_store_text == "입점신청"

    def test_favorite(self, setup) :
        # logger = self.get_logger()  # Baseclass에 선언한 로그를 불러오는 객체
        first_Topbanner = self.driver.find_element(By.XPATH, '//*[@id="coupang-banner"]/span/div/a[1]/img')
        second_Topbanner = self.driver.find_element(By.XPATH, '//*[@id="coupang-banner"]/span/div/a[2]/img')

        self.driver.find_element(By.XPATH,'//*[@id="coupang-banner"]/span/div/a[1]/img').click()

    #크롬, 파이어폭스, IE 순차 실행
    # def test_crossbrowser(self, browsercrosscheck) :
    #    print(self, browsercrosscheck)