
def index():
    with open("./templates/index.html") as f:
        content = f.read()
    return content

def center():
    with open("./templates/center.html") as f:
        content = f.read()
    return content

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=GBK')])

    file_name = env['PATH_INFO']
    # PATH_INFO:/index.py
    if file_name == "/index.py":
        return index()
    elif file_name == "/center.py":
        return center()
    else:
        return 'Hello World!  Jaso中国'