from test_case.test_loginCase import Login_Case
from test_case.online_case.test_online_ykb_case import Online_Ykb_Case
from test_case.leaguer_case.test_leaguer_level_case import Leaguer_Level_Case
from common import config_manage
import unittest
import HTMLTestRunner

login_test = unittest.TestLoader().loadTestsFromTestCase(Login_Case)
online_test = unittest.TestLoader().loadTestsFromTestCase(Online_Ykb_Case)
leaguer_level_test = unittest.TestLoader().loadTestsFromTestCase(Leaguer_Level_Case)

if __name__ == '__main__':
    # suites = unittest.TestSuite([online_test, login_test, leaguer_level_test])
    suites = unittest.TestSuite([leaguer_level_test])

    html_file = config_manage.REPORT_PATH + "TestResult_Report.html"  # 固定生成一份测试报告
    fp = open(html_file, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='游乐宝_Web自动化测试报告', description='用例执行情况:')
    runner.run(suites)
    fp.close()
