from django.shortcuts import render

# Create your views here.
from apps import models


def getUsers(request):
    userList = models.User.objects.all()
    return render(request, 'html/user.html', {'userList': userList})
