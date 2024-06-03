import pytest
from selenium import webdriver

from page_objects.login_page import LoginPage


@pytest.fixture(scope='class')
def driver():
    with webdriver.Chrome() as wd:
        # 最大化游览器
        wd.maximize_window()
        # 返回游览器对象，不能使用return，return返回之后会关闭游览器，无法进行后续操作
        yield wd
        wd.quit()

@pytest.fixture(scope='class')
# 参数名与上面的夹具同名
def logged_in_driver(driver):
    lp = LoginPage(driver)
    driver.get(lp.settings.PROJECT_HOST + lp.settings.INTERFACE['login'])
    lp.login(lp.settings.TEST_NORMAL_USERNAME, lp.settings.TEST_NORMAL_PASSWORD)
    yield driver
    # 返回webdriver