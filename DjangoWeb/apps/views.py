from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from apps import models


def getUsers(request):
    userList = models.User.objects.all()
    return render(request, 'html/user.html', {'userList': userList})


def addUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        e_mail = request.POST['email']
        models.User.objects.create(username=username, password=password, email=e_mail)
        return HttpResponseRedirect('/allUser/')
    else:
        return HttpResponse('数据添加不成功！')


def deleteUser(request):
    try:
        # 得到的id是string类型的，需要转成10进制的整形数据；同时还要区分是GET还是POST方法提交数据
        id = request.GET.get('id')
        # models.User.objects.filter(id=id).delete()
        models.User.objects.get(id=int(id)).delete()
        return HttpResponseRedirect('/allUser/')
    except:
        msg = '没有当前用户，删除错误！'
        return render(request, 'html/error.html', {'msg': msg})


def otherHtml(request):
    errorMsg = '城市信息列表暂时为空，信息收录中......'
    return render(request, 'html/city.html', {'errorMsg': errorMsg})
