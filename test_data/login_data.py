# 正向用例
success_cases = [
    {
        'title': "登录成功-管理员",
        'request_data': {"username": "test_admin", "password": "admin123"}
    }
]

# 反向用例
fail_cases = [
    {
        'title': "用户名为空",
        'request_data': {"username": "", "password": "admin123"},
        'warn_tip': "请输入用户名"
    },
    {
        'title': "密码为空",
        'request_data': {"username": "test_system_admin", "password": ""},
        'warn_tip': "请输入密码"
    }
]

# 用户名密码错误用例
error_cases = [
    {
        'title': "用户名或密码不正确",
        'request_data': {"username": "test_admin", "password": "Admin@12122"},
        'error_tip': "账户名或者密码错误"
    }
]