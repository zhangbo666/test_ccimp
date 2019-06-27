from django.shortcuts import render,HttpResponse

from ccimp_user_app.views import auth

from ccimp_permission_app.models.permissionClassModels import PermissionClass
from ccimp_user_app.models.userModels import User

# 用户权限
@auth
def permission_manage(request):

    if request.method == "GET":

        get_username = request.session.get('user','')

        users = User.objects.all()

        for user in users:

            if user.user_name == get_username:

                if user.permission_options == 1:

                    return render(request, "permission.html",
                                  {"username": get_username,
                                   "type": "list",
                                   "type_option": "permission_sap",
                                   "users": users})

                else:

                    return render(request, "404.html")


# 用户权限编辑
@auth
def edit_permission(request,uid):

    pass



'''###############################################################################'''

# 权限分类
@auth
def permission_class(request):

    get_username = request.session.get('user', '')

    permissionClasss = PermissionClass.objects.all()

    if request.method == "GET":

        users = User.objects.all()

        for user in users:

            if user.user_name == get_username:

                if user.permission_options == 1:

                   return render(request,"permission_class.html",
                              {"username":get_username,
                               "type":"list",
                               "type_option":"permission_sap",
                               "permissionClasss":permissionClasss})

                else:

                    return render(request,"404.html")

            else:

                pass

    else:

        return render(request,"permission_class.html",
                      {"username":get_username,
                       "type": "list",
                       "type_option":"permission_sap",
                       "permissionClasss": permissionClasss})

# 添加权限
@auth
def add_permissionClass(request):

    '''创建权限'''

    permission_chinese_names = PermissionClass.objects.all()

    permission_names = []

    username = request.session.get('user', '')

    # 返回前端非超级管理员信息
    for p1 in permission_chinese_names:

        if p1.permission_options != 1:

            permission_names.append(p1)

    if request.method == "GET":

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

    else:

        pc_name = request.POST.get("permission_chine_name","")

        pe_name = request.POST.get("permission_english_name","")

        po_name = request.POST.get("permission_options","")

        # po_name = request.POST.get("poName","")

        if po_name == "项目管理员" or po_name == "模块管理员" or po_name == "普通管理员":

            return render(request, "permission_class.html",{"username":username,"type":"add"})

        else:

            return render(request, "permission_class_add.html",{"username":username,"type":"add","po_name":"权限分类错误"})


# 编辑权限
@auth
def edit_permissionClass(request,pclass_id):

    '''编辑权限'''

    permissionclass = PermissionClass.objects.get(id=pclass_id)

    if request.method == "GET":

        return render(request,"permission_class_add.html",{"type":"add","permissionclass":permissionclass})
