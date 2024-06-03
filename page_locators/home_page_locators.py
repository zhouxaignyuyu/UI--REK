from selenium.webdriver.common.by import By


class HomePageLocators:
    '''
    首页面定位信息
    '''
    #退出按钮
    logout_loc = (By.CLASS_NAME,'ant-dropdown-menu-title-content')
    #退出确认按钮
    logout_confirm_loc=(By.CLASS_NAME,'ant-btn-primary')
    # 点击用户名
    Username_loc = (By.CLASS_NAME, 'ant-dropdown-trigger')
    #生产订单管理按钮
    Production_order_management_loc =(By.CLASS_NAME,"ant-menu-title-content")