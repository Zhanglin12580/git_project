from test_case.base_case import Base_Case
from po.pages.goods_menu.goods_add import add_goods
import unittest
test_data = {'商品名称': '牛刀小试',
             '商品价格': 10,
             '初始化库存': 10}
class goods_case(Base_Case):
    def test_001_goods_case(self):
        super().default_login()
        goods = add_goods(self.base,test_data)
        goods.switch_goodsmenu()
        goods.add_goods()
        self.flag = False

if __name__ == '__main__':
    unittest.main()
