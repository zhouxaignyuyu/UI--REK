from selenium.webdriver.common.by import By


class LoginPageLocators:
    '''
    登录页面的定位信息
    '''

    # 定位信息放到类属性中
    # 用户输入框定位
    username_input_locator = (By.ID, 'basic_loginName')
    # 密码输入框定位
    password_input_locator = (By.ID, 'basic_password')
    # 登录按钮定位
    login_btn_locator = (By.CLASS_NAME, 'login-btn')
    # 错误信息定位
    error_info_tip_loc = (By.CSS_SELECTOR, '.ant-form-item-explain-error')
    #用户名为空提示
    empty_username = (By.CLASS_NAME,"ant-form-item-explain-error")
    empty_password = (By.CSS_SELECTOR, ".ant-form-item-explain-error")
    #是否强制登录按钮
    is_login_loc = (By.XPATH,"//span[contains(.,'确 定')]")
    #关闭菜单指示按钮
    close_menu =(By.XPATH,"/html/body/div[3]/button")
    #账号或密码错误提示
    password_error_tip=(By.CLASS_NAME,'anticon-close-circle')

