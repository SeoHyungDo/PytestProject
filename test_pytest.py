def test_firstprogram() :
    print("Hello")

def test_secondprogram(conf) :
    a = 512312312321
    b = 312312123

    assert '9' in str(a)

#크롬, 파이어폭스, IE 순차 실행
def test_crossbrowser(BrowserCrosscheck) :
    print(BrowserCrosscheck)