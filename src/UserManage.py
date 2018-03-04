from src.models import insert,loadalluser,deletebyid
from src.User import user
from src.request import Request
from src.utils import template
from src.respone import  response_with_headers,redirect
from src.routes import route

path='../Data/userdata.txt'


@route('/')
def Index(request):
    rsc= template('index.html')
    header={
        'Content-Type':'text/html',
    }
    lines=loadalluser()
    text=''
    tr=''' <tr>
                    <td>{}</td>
                    <td class="am-hide-sm-only">{}</td>
                    <td class="am-hide-sm-only">{}</td>
                    <td>
                      <div class="am-btn-toolbar">
                        <div class="am-btn-group am-btn-group-xs">
                <a href='../Delete?id={}' class=' class="am-btn am-btn-default am-btn-xs am-text-danger am-hide-sm-only"'><span class="am-icon-trash-o"></span> 删除</a>
                        </div>
                      </div>
                    </td>
                  </tr>'''
    print("======================="+str(len(lines)))
    for u in lines:
        print(len(u))
        print(u[1])
        print(u[2])
        temp=tr.format(u[1],u[2],u[3],u[0])
        text+=temp
    return response_with_headers(header,code=200)+'r\n\r\n'+rsc.format(text)

@route('/Add')
def Add(request):
    rsc=template('add.html')
    header = {
        'Content-Type': 'text/html',
    }
    return response_with_headers(header, code=200) + 'r\n\r\n' + rsc

@route('/Add_Post')
def Add_Post(request):
      fromdata=request.form()
      name=fromdata.get('name','')
      email=fromdata.get('email','')
      phone=fromdata.get('phone','')
      u=user(id=1,name=name,email=email,phonenumber=phone)
      insert(u)
      return redirect('/')


@route('/Delete')
def  Delete(request):
    id=request.query.get('id',1)
    deletebyid(id)
    return  redirect('/')
@route('/Edit')
def  Edit(request):
    return "xiugai"

def Error(request):
    rsc = template('notfound.html')
    header = {
        'Content-Type': 'text/html',
    }
    return response_with_headers(header, code=404) + 'r\n\r\n' + rsc

