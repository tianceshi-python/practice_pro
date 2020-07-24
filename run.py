# encoding:utf-8


import pytest

if __name__ == '__main__':
    pytest.main(['-s', '-q','-m=conferenceControl_test', "--html=./result_html/reportname.html "])