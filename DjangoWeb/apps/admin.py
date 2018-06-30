from django.contrib import admin

# Register your models here.
from apps import models

# 在本地创建的User数据表apps_user中创建注册用户，默认在Django的auth_user中创建用户
admin.site.register(models.User)