# coding:utf-8
import unittest, time, os, sys, platform
from common.logger import Logger
from common import config_manage
from po.pages.base_page import Base_Page
from selenium.webdriver.common.by import By
from common.driver_manage import Driver_Manager

# 元素定位：文件名称
login_loc = config_manage.get_yaml_page_loc('login_loc.yaml')


class Base_Case(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        driver_manager = Driver_Manager()
        cls.driver = driver_manager.get_driver(login_loc['browserType'])

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        self.flag = True
        self.log = Logger()
        self.start = time.perf_counter()
        self.log.info("============【{}测试用例开始】====================".format(self.__class__.__name__))
        self.driver.implicitly_wait(10)
        self.base = Base_Page(self.driver, self.log)
        self.log.info("【操作系统】：" + str(platform.platform()))
        self.log.info("【浏览器】：" + login_loc['browserType'])
        self.driver.get(login_loc['URL_TEST'])
        self.log.info("【打开URL】：" + login_loc['URL_TEST'])
        self.base.wait(1)

    def tearDown(self) -> None:
        if (self.flag):
            # 异常截图
            self.base.screenshot_img(self._testMethodName)
        self.end = time.perf_counter()
        self.log.info('【用例运行时长】: {}秒'.format(self.end - self.start))
        self.log.info("====================【{}测试用例结束】====================".format(self.__class__.__name__))
        self.log.del_handler()  # 防止重复写入日志

    def default_login(self):
        self.base.input(By.XPATH, login_loc['登录页面']['用户名'], login_loc['数据']['用户名'])
        self.base.input(By.XPATH, login_loc['登录页面']['密码'], login_loc['数据']['密码'])
        self.base.click(By.XPATH, login_loc['登录页面']['登录按键'])
        self.base.wait(2)
        self.log.info("【默认登录成功】")
