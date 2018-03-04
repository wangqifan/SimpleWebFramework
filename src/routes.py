from src.respone import route_static



#路由装饰器
def route(url):
    def decorator(func):
        route_dict[url]=func
        return func
    return decorator


#路由表
route_dict = {
 #   '/': Index,
#    '/Index':Index,
#    '/Add':Add,
 #   '/Delete':Delete,
 #   '/Edit':Edit,
 #   'static':route_static,
 #   '/Add_Post':Add_Post,
}
