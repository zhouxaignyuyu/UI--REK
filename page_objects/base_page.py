# -*- coding: utf-8 -*-
# @Time    : 2023/3/24  14:26
# @Author  : jikkdy
# @FileName: base_page.py

import os, time
import re
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import settings
from common import logger


class BasePage:
    '''
    web自动化 稳定性
    selenium - chromedriver - 浏览器 - 服务器
    页面对象的基类
    封装常用操作
    节省代码量，便于维护
    1. 查找元素 等待 - 查找
    2. 点击 等待 - 查找 - 点击
    3. 输入 等待 - 查找 - 输入
    5. 获取元素文本 等待 - 查找 -获取文本
    6. 获取元素属性 等待 - 查找 -获取属性
    7. 窗口切换
    8. 失败截图
    '''
    # 将日志、配置文件定义为类属性
    name = 'base页面'
    logger = logger
    settings = settings

    # 内容初始化
    def __init__(self, driver: WebDriver):
        self.driver = driver
        # 初始化元素
        self.element = None
        # 初始化定位信息
        self.locator = None
        # 初始化动作描述
        self.action = ''


    def delay(self, second=0.5):
        '''
        延时操作
        :param second:秒  支持浮点数
        :return:
        '''
        time.sleep(second)
        # 定义返回对象，用于链式编程
        # 如：wait_element_is_visible(('xpath', '//input[@name="username"]'),action='输入用户名').delay(3).send_keys('11111')
        return self

    def wait_element_is_visible(self, locator, action='', **kwargs):
        '''
        等待元素可见
        :param locator:定位信息 tuple(by,expression)
        :param action: 操作说明 str
        :param kwargs: timeout（等待时间），poll_frequency（轮循时间）
        :return: page_object
        '''

        # 类属性定位信息和动作描述为None，则重新赋值，方便传递locator和action到下一个动作
        self.locator = locator
        self.action = action
        try:
            # 当有timeout参数时，使用传入的timeout值，否则使用默认的等待时长
            timeout = kwargs.get('timeout', self.settings.DEFAULT_TIMEOUT)
            # 当有poll_frequency时，使用传入参数，否是使用默认的时间间隔0.5s
            poll_frequency = kwargs.get('poll_frequency', 0.5)
            # 等待元素可见并返回element信息并定义为对象属性
            self.element = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            # 记录失败日志
            self.logger.exception('在{},{}操作的时候，等待{}元素可见【失败】'.format(self.name, action, locator))
            # 操作失败时保存截屏
            self.get_page_screenshot(action)
            raise e
        else:
            # 操作成功记录日志
            self.logger.debug('在{},{}操作的时候，等待{}元素可见【成功】'.format(self.name, action, locator))
            # 返回对象，便于链式编程
            return self

    def wait_element_to_be_clickable(self, locator, action='', **kwargs):
        '''
        等待元素可被点击
        :param locator:定位信息 tuple(by,expression)
        :param action:操作说明  str
        :param kwargs:timeout（等待时间），poll_frequency（轮循时间）
        :return:
        '''
        # 类属性定位信息和动作描述为None，则重新赋值，方便传递locator和action到下一个动作
        self.locator = locator
        self.action = action
        try:
            # 当有timeout参数时，使用传入的timeout值，否则使用默认的等待时长
            timeout = kwargs.get('timeout', self.settings.DEFAULT_TIMEOUT)
            # 当有poll_frequency时，使用传入参数，否是使用默认的时间间隔0.5s
            poll_frequency = kwargs.get('poll_frequency', 0.5)
            # 等待元素可点击并返回element信息并定义为对象属性
            self.element = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.element_to_be_clickable(locator))
        except Exception as e:
            # 记录失败日志
            self.logger.exception('在{},{}操作的时候，等待{}元素可点击【失败】'.format(self.name, action, locator))
            # 操作失败时保存截屏
            self.get_page_screenshot(action)
            raise e
        else:
            # 操作成功记录日志
            self.logger.debug('在{},{}操作的时候，等待{}元素可点击见【成功】'.format(self.name, action, locator))
            # 返回对象，便于链式编程
            return self

    def wait_elment_is_loaded(self, locator, action='', **kwargs):
        '''
        等待元素加载到dom中
        :param locator:定位信息 tuple(by,expression)
        :param action:操作说明  str
        :param kwargs:timeout（等待时间），poll_frequency（轮循时间）
        :return:
        '''
        # 类属性定位信息和动作描述为None，则重新赋值，方便传递locator和action到下一个动作
        self.locator = locator
        self.action = action
        try:
            # 当有timeout参数时，使用传入的timeout值，否则使用默认的等待时长
            timeout = kwargs.get('timeout', self.settings.DEFAULT_TIMEOUT)
            # 当有poll_frequency时，使用传入参数，否是使用默认的时间间隔0.5s
            poll_frequency = kwargs.get('poll_frequency', 0.5)
            # 等待元素加载到dom并返回element信息并定义为对象属性
            self.element = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(locator))
        except Exception as e:
            # 记录失败日志
            self.logger.exception('在{},{}操作的时候，等待{}元素加载到文档【失败】'.format(self.name, action, locator))
            # 操作失败时保存截屏
            self.get_page_screenshot(action)
            raise e
        else:
            # 操作成功记录日志
            self.logger.debug('在{},{}操作的时候，等待{}元素加载到文档【成功】'.format(self.name, action, locator))
            # 返回对象，便于链式编程
            return self

    def send_keys(self, content):
        '''
        输入字符串
        :param content: 输入的内容 str
        :return:
        '''
        # 防止在wait方法执行前调用send_keys方法
        if self.element is None:
            raise RuntimeError('不能在wait方法之前调用元素上的方法')
        try:
            # 输入之前清空输入框，防止预填
            self.element.clear()
            # 执行输入字符串操作
            self.element.send_keys(content)
        except Exception as e:
            # 定义操作失败日志
            self.logger.exception('在{},{}操作的时候，对{}元素输入{}【失败】'.format(self.name, self.action, self.locator, content))
            # 操作失败后截屏
            self.get_page_screenshot(self.action)
        else:
            # 操作成功后日志
            self.logger.debug('在{},{}操作的时候，对{}元素输入{}【成功】'.format(self.name, self.action, self.locator, content))
        finally:
            # 清空wait缓存：因执行send_keys方法后，会进行下一步其他操作，故需要清空action，locator等内容
            # 私有方法，仅在内部可调用
            self.__clear_cache()

    def get_element(self):
        '''
        获取元素
        :return:
        '''
        # 防止在wait方法执行前调用方法
        if self.element is None:
            raise RuntimeError('不能在wait方法之前调用元素上的方法')
        # 返回元素
        return self.element

    def click_element(self):
        '''
        点击元素
        :return:
        '''
        # 防止在wait方法执行前调用click方法
        if self.element is None:
            raise RuntimeError('不能在wait方法之前调用元素上的方法')
        try:
            # 执行操作
            self.element.click()
        except Exception as e:
            # 定义操作失败日志
            self.logger.exception('在{},{}操作的时候，点击元素{}【失败】'.format(self.name, self.action, self.locator))
            # 操作失败后截屏
            self.get_page_screenshot(self.action)
        else:
            # 操作成功后日志
            self.logger.debug('在{},{}操作的时候，点击元素{}【成功】'.format(self.name, self.action, self.locator))
        finally:
            # 清空wait缓存：因执行click方法后，会进行下一步其他操作，故需要清空action，locator等内容
            # 私有方法，仅在内部可调用
            self.__clear_cache()

    def click_elment_by_js(self):
        '''
        通过js点击元素
        :return:
        '''
        if self.element is None:
            raise RuntimeError('不能在wait方法之前调用元素上的方法')
        try:
            # 执行操作
            self.driver.execute_script('arguments[0].click()', self.element)
        except Exception as e:
            # 定义操作失败日志
            self.logger.exception('在{},{}操作的时候，点击元素{}【失败】'.format(self.name, self.action, self.locator))
            # 操作失败后截屏
            self.get_page_screenshot(self.action)
        else:
            # 操作成功后日志
            self.logger.debug(
                '在{},{}操作的时候，点击元素{}【成功】'.format(self.name, self.action, self.locator)
            )
        finally:
            # 清空wait缓存：因执行click方法后，会进行下一步其他操作，故需要清空action，locator等内容
            # 私有方法，仅在内部可调用
            self.__clear_cache()

    def get_element_text(self):
        '''
        获取元素的文本
        :return:
        '''
        # 防止在wait方法执行前调用获取元素属性方法
        if self.element is None:
            raise RuntimeError('不能在wait方法之前调用元素上的方法')
        try:
            # 执行操作
            value = self.element.text
        except Exception as e:
            # 定义操作失败日志
            self.logger.exception('在{},{}操作的时候，获取{}元素的文本【失败】'.format(self.name, self.action, self.locator))
            # 操作失败后截屏
            self.get_page_screenshot(self.action)
        else:
            # 操作成功后日志
            self.logger.debug('在{},{}操作的时候，获取{}元素的文本【成功】'.format(self.name, self.action, self.locator))
            # 返回value信息
            return value
        finally:
            self.__clear_cache()

    def get_element_attr(self, name):
        '''
        获取元素的属性
        :param name:要获取的属性名
        :return:
        '''
        # 防止在wait方法执行前调用获取元素属性方法
        if self.element is None:
            raise RuntimeError('不能在wait方法之前调用元素上的方法')
        try:
            # 执行操作
            value = self.element.get_attribute(name)
        except Exception as e:
            # 定义操作失败日志
            self.logger.exception('在{},{}操作的时候，获取{}元素的{}属性【失败】'.format(self.name, self.action, self.locator, name))
            # 操作失败后截屏
            self.get_page_screenshot(self.action)
        else:
            # 操作成功后日志
            self.logger.debug('在{},{}操作的时候，获取{}元素的{}属性【成功】'.format(self.name, self.action, self.locator, name))
            # 返回value信息
            return value
        finally:
            self.__clear_cache()

    def switch_to_new_window(self, handle=None, action=''):
        '''
        切换到新的窗口
        :param handle:窗口句柄
        :param action:
        :return:
        '''
        try:
            # 如果传入handle，则跳转到指定的窗口
            if handle:
                self.driver.switch_to.window(handle)
            else:
                # 获取当前窗口的句柄
                original_window = self.driver.current_window_handle
                # 循环当游览器的所有句柄
                for handle in self.driver.window_handles:
                    # 当句柄不等于当前句柄时，跳转句柄，进行窗口切换
                    if handle != original_window:
                        self.driver.switch_to.window(handle)
                        break
        except Exception as e:
            self.logger.exception('在{},{}操作的时候，切换到窗口{}【失败】'.format(self.name, self.action, handle))
            # 报错时截屏
            self.get_page_screenshot(action)
            raise e
        else:
            self.logger.exception(
                '在{},{}操作的时候，切换到窗口{}【成功】'.format(self.name, self.action, handle)
            )

    def get_page_screenshot(self, action):
        '''
        截图功能
        获取报错时的页面截图，命名规范： 截图时间_xx页面_xx操作
        :param action:
        :return:
        '''
        img_path = os.path.join(self.settings.ERROR_SCREENSHOT_DIR,'{}_{}_{}.png'.format(datetime.now().strftime('%Y-%m-%d %H-%M-%S'),self.name,action))
        self.driver.save_screenshot(img_path)
        if self.driver.save_screenshot(img_path):
            self.logger.info('生成错误截屏{}【成功】'.format(img_path))
        else:
            self.logger.info('生成错误截屏{}【失败】'.format(img_path))

    def replace_args_by_re(self, json_s, obj):
        '''
        通过正则表达式动态的替换参数
        :param json_s: 要替换的文本
        :param obj: 带有替换的文本
        :return:
        '''
        # 1.找出所有的槽位中的变量名(若公司项目中#为特殊字符，可将用例和此次#替换为其他特殊符号
        args = re.findall('#(.*?)#', json_s)
        for arg in args:
            # 2.找到obj中对应的属性,若无对应的属性，则返回None
            value = getattr(obj, arg, None)
            if value:
                json_s = json_s.replace('#{}#'.format(arg), str(value))
        return json_s

    def __clear_cache(self):
        '''
        清空wait的缓存
        :return:
        '''
        self.element = None
        self.locator = None
        self.action = ''

    def refresh(self):
        self.driver.refresh()

# if __name__ == '__main__':
#     from selenium import webdriver
#
#     with webdriver.Chrome() as driver:
#         page = BasePage(driver)
#         page.driver.get('http://testingedu.com.cn:8000/Home/user/login.html')
#         # 链式编程
#         page.wait_element_is_visible(('xpath', '//input[@name="username"]'), action='输入用户名').delay(3).send_keys('11111')