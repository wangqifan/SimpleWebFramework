# SimpleWebFramework
building webserice with socket


项目介绍 
------
本项目使用socket构架web服务，没有使用web服务器。
原理介绍
------
http协议是基于tcp协议的应用层协议，请求一下，响应一下。一个请求过来首先解析请求生成http请求对象来保存相关信息
‘’‘
GET / HTTP/1.1
Host: 127.0.0.1:3000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
’‘’




