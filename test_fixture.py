import pytest

#통상 conftest에 선언한 픽스쳐를 불러온다.
@pytest.mark.usefixtures("conf")

class Test :

    def test_fixture(self):
        print ("Message")


    def test_fixture1(self):
        print ("Message 1")


    def test_fixture2(self):
        print ("Message 2")


    def test_fixture3(self):
        print ("Message 3")