# coding:utf-8
from test_case.base_case import Base_Case
from po.pages.leaguer_menu.leaguer_level_page import Leaguer_Level_Page
import unittest

test_data = {'级别名称': 'atuo级别', '续期价格': 10, '补卡价格': 10, '积分过期时长': 2, '注销退款系数':1,
             '换卡价格': 2, '备注': '备注1', '预期结果': '保存成功'}


# @unittest.skip()
class Leaguer_Level_Case(Base_Case):

    def test_001_leaguer_level_case(self):
        super().default_login()
        leaguer_level_page = Leaguer_Level_Page(self.base, test_data)
        leaguer_level_page.switch_in_leaguer_level_menu()
        leaguer_level_page.click_add_btn()
        leaguer_level_page.input_info()
        leaguer_level_page.click_save_btn()
        leaguer_level_page.assert_info()

        self.flag = False


if __name__ == '__main__':
    unittest.main()
