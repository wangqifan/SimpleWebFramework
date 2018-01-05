from src.request import Request
from src.utils import log

def response_with_headers(headers, code=200):
    """
    Content-Type: text/html
    """
    header = 'HTTP/1.1 {} VERY OK\r\n'.format(code)
    header += ''.join(['{}: {}\r\n'.format(k, v)
                       for k, v in headers.items()])
    return header

def redirect(url):
    header={
        "Location":url,
    }
    return response_with_headers(header,code=302)


dict_type={
        'html':'text/html; charset=utf-8',
         'css':'text/css',
        'js':'application/javascript'
    }

def route_static(request):
    """
    静态资源的处理函数
    """
    filename = request.query.get('filename','/static/index.html')
    filetype=''

 #   try:
    filetype=filename.split('.')[-1]
  #  except:
      #  filetype = 'html'

    log('filetype============',filetype)
    res=''
    path = '../' + filename
    content_type=dict_type.get(filetype,'text/plain')
    with open(path, 'rb') as f:
          header = 'HTTP/1.1 200 OK\r\nContent-Type:{}\r\n\r\n'.format(content_type)
          res= header + str(f.read(),encoding='utf-8')
    return res
