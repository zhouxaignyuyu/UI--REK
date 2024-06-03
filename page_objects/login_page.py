import settings
from page_objects.base_page import BasePage
from page_locators.login_page_locators import LoginPageLocators as loc


class LoginPage(BasePage):
    name = '登录页面'

    def login(self, username, password):
        '''
        登录页面的登录功能
        :param username:
        :param password:
        :param verify:
        :return:
        '''

        # 1.访问登录页面
        self.driver.get(settings.PROJECT_HOST + settings.INTERFACE['login'])
        # 2.输入用户名、密码和验证码
        # 链式调用，需自己封装 在方法中返回self
        # 2.1输入用户名
        self.wait_element_is_visible(locator=loc.username_input_locator, action='输入用户名').send_keys(username)
        # 2.2 输入密码
        self.wait_element_is_visible(locator=loc.password_input_locator, action='输入密码').send_keys(password)
        # 3.点击登录按钮
        self.wait_element_is_visible(locator=loc.login_btn_locator, action='点击登录按钮').click_element()
        if (username!='' and password!=''):
            # 4.强制登录
            self.wait_element_is_visible(locator=loc.is_login_loc,action='是否强制登录').click_element()
            # 5.关闭菜单指引
            self.wait_element_is_visible(locator=loc.close_menu,action='关闭菜单指引按钮').click_element()

    def get_empty_warn(self, warn_tip):
        if warn_tip == '请输入用户名':
            return self.wait_element_is_visible(locator=loc.empty_username,action='检查用户名为空提示').get_element_text()
        elif warn_tip == '请输入密码':
            return self.wait_element_is_visible(locator=loc.empty_password,action='检查密码为空提示').get_element_text()
        elif warn_tip == '账户名或者密码错误':
            return self.wait_element_is_visible(locator=loc.password_error_tip,action='检查账户或密码错误提示').get_element_text()
