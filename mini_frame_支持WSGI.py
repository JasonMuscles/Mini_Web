def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=GBK')])
    return 'Hello World!  Jaso中国'