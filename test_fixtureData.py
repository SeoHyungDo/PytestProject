import pytest

@pytest.mark.usefixtures("Precondition_data")
class TestExample2 :

    def test_editProfile(self, Precondition_data):
        print(Precondition_data[0]) # 픽스쳐에 등록된 사전조건 인덱스의 첫번째를 가져온다.
        print(Precondition_data[1]) # 픽스쳐에 등록된 사전조건 인덱스의 두번째를 가져온다.
        print(Precondition_data[2]) # 픽스쳐에 등록된 사전조건 인덱스의 세번째를 가져온다.