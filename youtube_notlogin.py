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

driver.get("https://www.youtube.com")
chrome_option.add_argument("—ignore-certificate-errors") #인증 오류 무시
driver.maximize_window()

#브라우저의 타이틀을 받아옴
browser_title = driver.title
print("받아온 브라우저 타이틀 ==> " + browser_title)
assert(browser_title == "YouTube"), "YouTube Title 불일치"

#브라우저의 URL을 받아옴
browser_Url = driver.current_url
print("받아온 브라우저 URL ==> " + browser_Url)
assert(browser_Url == "https://www.youtube.com/"), "유튜브 URL 불일치"

try :
    if driver.find_element(By.ID, "guide-button").is_displayed() :
        print("guide-button 노출 확인!")

except Exception as e :
    print("Guide-button 미 노출")

# dropdown = Select(driver.find_element(By,)) 드롭다운 테스트
# selenium.webdriver.support.select.Select 임포트

time.sleep(10)
driver.close()
