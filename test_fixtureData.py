import pytest

@pytest.mark.usefixtures("Precondition_data")
class TestExample2 :

    def test_editProfile(self, Precondition_data):
        print(Precondition_data)