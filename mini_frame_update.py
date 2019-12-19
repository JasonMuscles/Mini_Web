import time


def login():
    return "欢迎登陆！ 现在时刻：%s" % time.ctime()


def register():
    return "欢迎注册！ 现在时刻：%s" % time.ctime()


def profile():
    return "欢迎进入个人信息页面！ 现在时刻：%s" % time.ctime()


def application(file_name):
    if file_name == "/login.py":
        return login()
    elif file_name == "/register.py":
        return register()
    else:
        return "not found you page..."
