import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture()
def conf() :
    print("this is first message")

@pytest.fixture(params=[("chrome","Seo"),"Firefox","IE"]) # 각 브라우저 크로스체크 픽스쳐 설정
def BrowserCrosscheck(request) :
    return request.param

# 사전조건으로 불러올 픽스쳐를 별도로 생성한다.
@pytest.fixture()
def Precondition_data() :
    print("사용자 프로필 데이터 생성 중.....")
    return ["Seo", "HyungDo", "May 2nd"]

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.coupang.com/")
    driver.maximize_window()
    # service_obj = Service(r"\Users\tjg10\PycharmProjects\PythonProject\Chromedriver.exe")
    # Mac의 경우 Chromedriver만 쓰면 됨, .exe는 윈도우에서 기재
    chrome_option = webdriver.ChromeOptions()
    # headless, SSL 오류 패스를 위한 chrome_option 선언
    # driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(10)
    request.cls.driver = driver  # 여기서 선언한 객체가 클래스로 보내짐, 해당 문이 있으면 return 필요 없음

    yield  # 테스트 종료 후
    driver.close()  # 브라우저를 닫아줌