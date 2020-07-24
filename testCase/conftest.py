# encoding:utf-8

from datetime import datetime
from py._xmlgen import html
import pytest
import re
import sys
import importlib
importlib.reload(sys)



@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    '''
    修改Description里面的内容，增加中文显示
    '''
    # pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    _description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")
    report._nodeid = _description

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.insert(2, html.th('Test_nodeid'))
    # cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop(2)

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report._nodeid))
    cells.insert(2, html.td(report.nodeid))
    # cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop(2)

