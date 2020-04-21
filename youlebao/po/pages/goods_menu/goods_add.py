import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from common import config_manage
goodsyaml = config_manage.get_yaml_page_loc('goods_loc\\add_goods.yaml')
class add_goods():
    def __init__(self,Base_Page,test_data):
        self.Base_Page= Base_Page
        self.test_data =test_data
    def switch_goodsmenu(self):
        '''进入商品新增菜单'''
        self.Base_Page.click(By.XPATH,goodsyaml['商品'])
        self.Base_Page.click(By.XPATH, goodsyaml['商品管理'])
        self.Base_Page.wait(2)
        self.Base_Page.click(By.XPATH, goodsyaml['商品资料'])
        self.Base_Page.switch_in_iframe(goodsyaml['商品资料iframe'])
    def add_goods(self):
        '''新增商品'''
        self.Base_Page.click(By.XPATH,goodsyaml['新增'])
        self.Base_Page.click(By.XPATH,goodsyaml['零售商品'])
        self.Base_Page.input(By.XPATH,goodsyaml['商品名称'],self.test_data['商品名称'])
        self.Base_Page.click(By.XPATH,goodsyaml['选择分类'])
        self.Base_Page.wait(1)
        self.Base_Page.click(By.XPATH,goodsyaml['商品分类'])
        self.Base_Page.input(By.XPATH,goodsyaml['商品价格'],self.test_data['商品价格'])
        self.Base_Page.input(By.XPATH, goodsyaml['初始化库存'],self.test_data['初始化库存'])
        self.Base_Page.click(By.XPATH,goodsyaml['保存'])
