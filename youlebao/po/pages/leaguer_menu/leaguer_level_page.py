# coding:utf-8
from selenium.webdriver.common.by import By
from common import config_manage
from common.sql_helper import Sql_Helper

leaguer_evel_loc = config_manage.get_yaml_page_loc('leaguer_loc\\leaguer_level_loc.yaml')


class Leaguer_Level_Page():
    def __init__(self, Base_Page, test_data):
        self.base = Base_Page
        self.data = test_data
        self.sql_assert = Sql_Helper()

    def switch_in_leaguer_level_menu(self):
        self.base.click(By.XPATH, leaguer_evel_loc["会员菜单"])
        self.base.click(By.XPATH, leaguer_evel_loc["会员管理菜单"])
        self.base.wait(1)
        self.base.click(By.XPATH, leaguer_evel_loc["会员级别菜单"])
        self.base.switch_in_iframe(leaguer_evel_loc["右侧iframe"])
        self.base.wait(2)

    def click_add_btn(self):
        self.base.click(By.XPATH, leaguer_evel_loc["新增按键"])

    def input_info(self):
        self.base.input(By.XPATH, leaguer_evel_loc["级别名称"], self.data["级别名称"])
        self.base.clear_and_input(By.XPATH, leaguer_evel_loc["续期价格"], self.data["续期价格"])
        self.base.clear_and_input(By.XPATH, leaguer_evel_loc["补卡价格"], self.data["补卡价格"])
        self.base.clear_and_input(By.XPATH, leaguer_evel_loc["积分过期时长"], self.data["积分过期时长"])
        self.base.clear_and_input(By.XPATH, leaguer_evel_loc["注销退款系数"], self.data["注销退款系数"])
        self.base.clear_and_input(By.XPATH, leaguer_evel_loc["换卡价格"], self.data["换卡价格"])
        self.base.input(By.XPATH, leaguer_evel_loc["备注"], self.data["备注"])
        self.base.wait(2)

    def click_save_btn(self):
        self.base.click(By.XPATH, leaguer_evel_loc["保存按键"])

    def assert_info(self):
        assert self.base.exists_element(By.XPATH, leaguer_evel_loc["保存提示"]) == True
        text = self.base.get_text(By.XPATH, leaguer_evel_loc["保存提示"])
        self.base.log.info("【保存提示】:" + str(text))
        sql = leaguer_evel_loc["sql断言"] + "'" + self.data["级别名称"] + "'"
        result = self.sql_assert.ExecQuery(sql)
        self.base.log.info("【数据库检查结果】:" + str(result))
        assert result is not None
        assert result[0]['LevelName'] == self.data["级别名称"]

        # assert self.data in text
