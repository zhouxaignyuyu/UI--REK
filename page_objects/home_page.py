from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_locators.home_page_locators import HomePageLocators as loc
from page_objects.base_page import BasePage


class HomePage(BasePage):
    '''
    首页
    '''
    name = '首页'

    # 定位信息放到类属性中
    def __init__(self, driver):
        self.driver = driver

    def click_logout_button(self):
        '''
        用户名
        :return:
        '''
        # 返回退出按钮的元素，若无返回则报错
        try:

            self.wait_element_is_visible(locator=loc.Username_loc,action='在用户名上点击').click_element()
            return self.wait_element_is_visible(locator=loc.logout_loc, action='点击退出按钮').click_element()
        except Exception as e:
            return None

    def get_user_value(self):
        try:
            return self.wait_element_is_visible(locator=loc.Username_loc, action='查看用户名是否正确').get_element_text()
        except Exception as e:
            return None

    def get_ProductionOrderManagement_value(self):
        try:
            return self.wait_element_is_visible(locator=loc.Production_order_management_loc, action='查看主页的生产订单管理').get_element_text()
        except Exception as e:
            return None