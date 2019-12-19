
def index():
    return "主页信息"

def login():
    return "登录页面"

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=GBK')])

    file_name = env["PATH_INFO"]
    # PATH_INFO:/index.py

    if file_name == "/index.py":
        return index()
    elif file_name == "/login.py":
        return login()
    else:
        return 'Hello World!  Jaso中国'