# SimpleWebFramework
building webserice with socket


项目介绍 
------


本项目使用socket构架web服务，没有使用web服务器。





原理介绍
------




http协议是基于tcp协议的应用层协议，请求一下，响应一下。一个请求过来首先解析请求生成http请求对象来保存相关信息</br>
```
GET / HTTP/1.1
Host: 127.0.0.1:3000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
```
这是一个典型的http请求，解析模块处理之后会得到，方式是Get，请求路径是‘/’。，求http请求版本是1.1(没用的信息)，以及浏览器的其他信息，解析代码如下
```

def path_parise(path):
    log(path)
    query={}
    index = path.find('?'）
    if index != -1:
        path, query_string = path.split('?', 1)
        args = query_string.split('&')
        query = {}
        for arg in args:
            k, v = arg.split('=')
            query[k] = v
    if 'static' in path:
        query['filename'] =path
        path='static'
    return path, query


```
解析后进入路由模块，根据路径查找路由表，找到对应的处理函数
```
route_dict = {
    '/': Index,
    '/Index':Index,
    '/Add':Add,
    '/Delete':Delete,
    '/Edit':Edit,
    'static':route_static,
    '/Add_Post':Add_Post,
}

```

静态文件的获取
```
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
    try:
        filetype=filename.split('.')[-1]
    except:
         filetype = 'html'
    res=''
    path = '../' + filename
    content_type=dict_type.get(filetype,'text/plain')
    with open(path, 'rb') as f:
          header = 'HTTP/1.1 200 OK\r\nContent-Type:{}\r\n\r\n'.format(content_type)
          res= header + str(f.read(),encoding='utf-8')
    return res
```
重定向的实现
```
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
```


