from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib import messages

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

# 权限分类list
@auth
def permission_class(request):

    '''权限分类list'''

    get_username = request.session.get('user', '')

    permissionClasss = PermissionClass.objects.all()

    if request.method == "GET":

        users = User.objects.all()

        for user in users:

            if user.user_name == get_username:

                if user.permission_options == 1:

                    print (type(user.create_time),user.create_time)
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

# 添加权限分类
@auth
def add_permissionClass(request):

    '''创建权限分类'''

    permission_chinese_names = PermissionClass.objects.all()

    get_username = request.session.get('user', '')

    if request.method == "GET":

        user = User.objects.get(user_name=get_username)

        permissionClasss = PermissionClass.objects.all()

        if user.user_name == get_username:

            if user.permission_options == 1:

                    return render(request,"permission_class_add.html",
                                  {"username":get_username,
                                   "type":"add",
                                   "type_option":"permission_sap"})

            else:

                return render(request,"404.html")

        else:

            pass

    else:

        pc_name = request.POST.get("permission_chine_name", "")
        pe_name = request.POST.get("permission_english_name", "")
        po_name = request.POST.get("permission_options", "")

        if pc_name == "":

            return render(request, "permission_class_add.html", {"username": get_username,
                                                                 "type": "add",
                                                                 "type_option": "permission_sap",
                                                                 "pc_name": "权限名称不能为空！"})
        elif pe_name == "":

            return render(request, "permission_class_add.html", {"username": get_username,
                                                                 "type": "add",
                                                                 "type_option": "permission_sap",
                                                                 "pe_name": "权限英文不能为空！"})

        elif po_name == "":

            return render(request, "permission_class_add.html", {"username": get_username,
                                                                 "type": "add",
                                                                 "type_option": "permission_sap",
                                                                 "po_name": "权限分类不能为空！"})

        if po_name == "项目管理员" or po_name == "模块管理员" or po_name == "普通管理员":

            if po_name == "项目管理员":

                po_name = 2

            elif po_name == "模块管理员":

                po_name = 3

            elif po_name == "普通管理员":

                po_name = 4

            PermissionClass.objects.create(permission_chinese_name=pc_name,
                                           permission_english_name=pe_name,
                                           permission_options=po_name)

            return HttpResponseRedirect("/permission/class/")

        else:

            return render(request, "permission_class_add.html", {"username": get_username,
                                                                 "type": "add",
                                                                 "type_option": "permission_sap",
                                                                 "po_name": "权限分类数据错误，请查看原因！"})


# 编辑权限分类
@auth
def edit_permissionClass(request,pclass_id):

    '''编辑权限分类'''

    permissionclass = PermissionClass.objects.get(id=pclass_id)

    get_username = request.session.get('user', '')

    if request.method == "GET":

        return render(request,"permission_class_edit.html",
                      {"username":get_username,
                       "type": "edit",
                       "type_option":"permission_sap",
                       "permissionClasss": permissionclass})