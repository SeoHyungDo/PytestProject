import time
from idlelib.search import find_selection

import selenium.webdriver.support.select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import youtube_account

from selenium.webdriver.common.by import By

#Mac의 경우 Chromedriver만 쓰면 됨, .exe는 윈도우에서 기재
service_obj = Service(r"\Users\tjg10\PycharmProjects\PythonProject\Chromedriver.exe")
#headless, SSL 오류 패스를 위한 chrome_option 선언
chrome_option = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service_obj)
action = ActionChains(driver) # ActionChains 선언

driver.get("https://www.coupang.com")
chrome_option.add_argument("—ignore-certificate-errors") #인증 오류 무시
driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="subscribeHeader"]/li[2]/a').click()
apply_store_select_box = driver.find_elements(By.XPATH,'//*[@id="subscribeHeader"]/li[2]')
for select_box_text in apply_store_select_box :
    apply_store_select_box_text = select_box_text.text
    print("selectbox 내의 텍스트 목록 : " + apply_store_select_box_text)

time.sleep(10)
driver.close()
