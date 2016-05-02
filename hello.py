def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    body = []
    qs_str = environ['QUERY_STRING']
    qs_strs = qs_str.split('&')
    for i in qs_strs:
        body.append(i+"\r\n")
    start_response(status, headers)
    return body
