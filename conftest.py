#Fixture는 TC의 초기화와 해제 코드로 사용된다
#yield 뒤에는 마지막에 사용될 코드를 입력한다

import pytest

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

