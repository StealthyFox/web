from cgi import parse_qs
def application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    body = []
    query = parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
	body = []
	for key, values in query.items():
		for item in values:
			body.append(key + "=" + item + "\r\n")

    
    #qs_str = environ['QUERY_STRING']
    #qs_strs = qs_str.split('&')
    #for i in qs_strs:
        #body.append(i+"\r\n")
    start_response(status, headers)
    return body
