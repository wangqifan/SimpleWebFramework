import socket
from src.request import Request
from src.utils import log
from src.routes import route_dict
from src.UserManage import Error

request = Request()
#url解析
def path_parise(path):
    log(path)
    query={}
    index = path.find('?')
    log('-----------------')
    log(index)
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

#响应
def response_for_path(path):
    log("the path is {}".format(path))
    response=route_dict.get(path,Error)
    return response(request)


def run(host='', port=3000):
    """module 'urllib' has no attribute 'parse'
    启动服务器
    """
    # 初始化 socket
    # 使用 with 可以保证程序中断的时候正确关闭 socket 释放占用的端口
    log('start at', '{}:{}'.format(host, port))
    with socket.socket() as s:
        s.bind((host, port))
        # 无限循环来处理请求
        while True:
            # 监听 接受 读取请求数据 解码成字符串
            s.listen(3)
            connection, address = s.accept()
            r = connection.recv(1000)
            r = r.decode('utf-8')
            log('ip and request, {}\n{}'.format(address, r))
            if len(r.split()) < 2:
                continue
            path = r.split()[1]
            # 设置 request 的 method
            request.method = r.split()[0]
            request.add_headers(r.split('\r\n\r\n', 1)[0].split('\r\n')[1:])
            #把body 放入 request 中
            request.body = r.split('\r\n\r\n', 1)[1]
            # 用 response_for_path 函数来得到 path 对应的响应内容
            path,query=path_parise(path)
            request.path=path
            request.query=query
            response = response_for_path(path)
            log('debug **', 'sendall')
            # 把响应发送给客户端
            connection.sendall(bytes(response,encoding='utf-8'))
            connection.close()


if __name__ == '__main__':
    # 生成配置并且运行程序
    config = dict(
        host='',
        port=3000,
    )
    run(**config)