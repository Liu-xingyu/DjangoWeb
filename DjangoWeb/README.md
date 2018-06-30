python的web开发框架django应用<br>
1.创建项目
django-admin createproject django-demo1

2.创建项目文件框架(如同MVC)
python manage.py startapp apps

3.python3.x版本使用mysql，需要早__init__.py文件中加入
pymysql.install_as_MySQLdb()

4.注册admin用户到User模型对应的数据库中
admin.site.register(models.User)

5.整合资源
python manage.py makemigrations

6.生成文件和数据库信息
python manage.py migrate

7.创建一个超级用户
python manage.py createsuperuser

8.启动Django项目
python manage.py runserver

9.配置加载如css、js、image等静态资源
STATICFILS_DIRS=[
    os.path.join(BASE_DIR,'static'),
]

10.配置不同数据库(以mysql数据库为例)
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'python_database',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}

11.重定向跳转执行制定的URL地址中的action
HttpResponseRedirect('/redirectUrl/')，redirectUrl为重定向的请求地址
