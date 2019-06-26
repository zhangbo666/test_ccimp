from django.shortcuts import render

from ccimp_user_app.views import auth

from ccimp_permission_app.models.permissionClassModels import PermissionClass
from ccimp_user_app.models.userModels import User

# 用户权限
@auth
def permission_manage(request):

    if request.method == "GET":

        username = request.session.get('user','')

        user = User.objects.get(user_name=username)

        permissions = PermissionClass.objects.all()

        if user.user_name == username:

            if user.permission_options == 1:

                return render(request,"permission.html",
                              {"username":username,
                               "type":"list",
                               "type_option":"permission_sap",
                               "permissions":permissions})

            else:

                return render(request,"404.html")
        else:

            pass


# 权限分类
@auth
def permission_class(request):

    if request.method == "GET":

        username = request.session.get('user','')

        user = User.objects.get(user_name=username)

        permissionClasss = PermissionClass.objects.all()

        if user.user_name == username:

            if user.permission_options == 1:

               return render(request,"permission_class.html",
                          {"username":username,
                           "type":"list",
                           "type_option":"permission_sap",
                           "permissionClasss":permissionClasss})

            else:

                return render(request,"404.html")

        else:

            pass


# 添加权限
@auth
def add_permissionClass(request):

    '''创建权限'''

    permission_chinese_names = PermissionClass.objects.all()

    permission_names = []

    # 返回前端非超级管理员信息
    for p1 in permission_chinese_names:

        if p1.permission_options != 1:

            permission_names.append(p1)

    if request.method == "GET":

        username = request.session.get('user','')

        user = User.objects.get(user_name=username)

        permissionClasss = PermissionClass.objects.all()

        if user.user_name == username:

            if user.permission_options == 1:

                    return render(request,"permission_class_add.html",
                                  {"username":username,
                                   "type":"add",
                                   "type_option":"permission_sap",
                                   "permission_names":permission_names})

            else:

                return render(request,"404.html")

        else:

            pass


# 编辑权限
@auth
def edit_permissionClass(request,pclass_id):

    '''编辑权限'''

    permissionclass = PermissionClass.objects.get(id=pclass_id)

    if request.method == "GET":

        return render(request,"permission_class_add.html",{"type":"add","permissionclass":permissionclass})
