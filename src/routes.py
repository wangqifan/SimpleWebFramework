from src.UserManage import *
from src.respone import route_static



#路由表
route_dict = {
    '/': Index,
    '/Index':Index,
    '/Add':Add,
    '/Delete':Delete,
    '/Edit':Edit,
    'static':route_static,
    '/Add_Post':Add_Post,
}