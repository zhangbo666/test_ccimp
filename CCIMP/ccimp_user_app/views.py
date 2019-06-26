#!/usr/bin/python
#encoding:utf-8

from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect

from ccimp_user_app.forms import UserLoginForm,UserRegisterForm
from django.contrib.auth.decorators import login_required
from ccimp_user_app.models.userModels import User


# 判断用户登录的装饰器
def auth(func):

    def inner(request, *args, **kwargs):
        v = request.session.get('is_login', None)
        if v != True:
            return redirect('/login_ccimp/')
        return func(request, *args, **kwargs)

    return inner


# 灵猫智能管理平台登录页
def index(request):

    '''
    灵猫智能管理平台登录页
    '''
    login_obj = UserLoginForm()

    return render(request,"login_ccimp.html",{'login_obj':login_obj})


# 用户登录页
def login_ccimp(request):

    '''
    登录动作
    '''

    if request.method == "GET":

        login_obj = UserLoginForm()

        return render(request,'login_ccimp.html',{'login_obj':login_obj})

    else:

        login_obj = UserLoginForm(request.POST)

        if login_obj.is_valid():

            get_user_name = request.POST.get("user_name", "")
            get_password  = request.POST.get("password", "")

            try:

                user_name = User.objects.get(user_name=get_user_name).user_name
                # print (type(user_name))
                # print (user_name)
                password = User.objects.get(user_name=get_user_name).password
                # print (type(password))
                # print (password)


                if get_password == password:

                    request.session['is_login'] = True

                    request.session['user'] = user_name

                    request.session.set_expiry(6000)

                    return HttpResponseRedirect("/project/")

                else:

                    return render(request, 'login_ccimp.html',
                              {"account_info": "*用户名或密码错误，请重新输入", 'login_obj': login_obj})

            except:

                return render(request, 'login_ccimp.html',
                              {"account_info": "*用户名或密码错误，请重新输入", 'login_obj': login_obj})


# 用户注册页
def register(request):

    '''
    灵猫智能管理平台注册页
    '''
    register_obj = UserRegisterForm()

    if request.method == "GET":

        return render(request,'register_ccimp.html',{'register_obj':register_obj})

    else:

        get_user_name = request.POST.get("user_name","")
        get_password  = request.POST.get("password","")
        get_real_name = request.POST.get("real_name","")
        get_mail      = request.POST.get("mail","")

        if get_user_name == "":

            return render(request, 'register_ccimp.html', {'name_error':"账户输入为空，请重新输入"})

        elif get_password == "":

            return render(request, 'register_ccimp.html', {'password_error':"密码输入为空，请重新输入"})

        elif get_real_name == "":

            return render(request, 'register_ccimp.html', {'real_name_error':"姓名输入为空，请重新输入"})

        elif get_mail == "":

            return render(request, 'register_ccimp.html', {'password_error':"邮件地址输入为空，请重新输入"})

        else:

            try:

                if User.objects.get(user_name=get_user_name):

                    return render(request,'register_ccimp.html',
                                  {"user_name_uplicate":"*注册账户重复",
                                   'register_obj':register_obj})

            except:

                try:

                    if User.objects.get(mail=get_mail):

                        return render(request,'register_ccimp.html',
                          {"mail_uplicate":"*注册邮箱重复",'register_obj':register_obj})

                except:

                    User.objects.create(user_name=get_user_name,
                                        password=get_password,
                                        real_name=get_real_name,
                                        mail=get_mail)

                    request.session['is_login'] = True

                    request.session['user'] = get_user_name

                    return HttpResponseRedirect("/project/")


# 退出系统
def logout(request):

    request.session['is_login'] = False

    return HttpResponseRedirect("/login_ccimp/")










