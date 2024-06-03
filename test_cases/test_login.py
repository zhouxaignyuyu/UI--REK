import pytest

import settings
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from test_cases.base_case import BaseCase
from test_data.login_data import *


class TestLogin(BaseCase):
    name = '登录功能'
    @pytest.mark.parametrize('case', success_cases)
    def test_login_success(self, driver, case):
        self.logger.info('***{}用例开始测试***'.format(case['title']))
        # 1.打开登录页面,拼接url
        driver.get(self.settings.PROJECT_HOST + settings.INTERFACE['login'])
        # 2.登录
        lp = LoginPage(driver)
        lp.login(case['request_data']['username'],case['request_data']['password'])
        # 3.断言是否登录成功
        hp = HomePage(driver)
        assert hp.get_ProductionOrderManagement_value()
        try:
        # 断言
            assert hp.get_ProductionOrderManagement_value() == '生产订单管理'
        except Exception as e:
            self.logger.exception('断言失败')
            raise e
        else:
            self.logger.info('***{}用例通过测试***'.format(case['title']))
            hp.click_logout_button()
        self.logger.info('***{}用例结束测试***'.format(case['title']))

    @pytest.mark.parametrize('case', fail_cases)
    def test_login_fail(self, driver, case):
        self.logger.info('***{}用例开始测试***'.format(case['title']))
        # 1.打开登录页面,拼接url
        driver.get(self.settings.PROJECT_HOST + settings.INTERFACE['login'])
        # 2.登录
        lp = LoginPage(driver)
        lp.login(case['request_data']['username'],case['request_data']['password'])

        try:
        # 断言
            assert lp.get_empty_warn(case['warn_tip']) == case['warn_tip']
        except Exception as e:
            self.logger.exception('断言失败')
            raise e
        else:
            self.logger.info('***{}用例通过测试***'.format(case['title']))
        #刷新以清空数据框
        lp.refresh()
        self.logger.info('***{}用例结束测试***'.format(case['title']))

