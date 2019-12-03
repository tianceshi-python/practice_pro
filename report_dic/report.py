# encoding:utf-8
import  pytest


def testTrue():
    assert  True


def testFalse():
    assert False

def testError():
    1 / 0


@pytest.mark.skip(reason='misunderstood the API')
def testSkip():
    assert 1 ==1


@pytest.mark.skip(reason='Xpass')
def testXPass():
    assert True

@pytest.mark.skip(reason='XFail')
def testXFail():
    assert False


if __name__ == "__main__":
    pytest.main(["-s", "report.py", "--pytest_report", "pytest_tian_Report.html"])


'''
if __name__ == '__main__':
    pytest.main(["-s","pytest_Demo.py","--pytest_report","pytest_tian_Report.html",'--pytest_title','report title','--pytest_desc','report desc','--pytest_theme','new_theme'])
'''
