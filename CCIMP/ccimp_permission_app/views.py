from django.shortcuts import render

from ccimp_user_app.views import auth

from ccimp_user_app.models.userPermissionModels import UserPermission

from ccimp_user_app.models.userModels import User

# 权限管理
@auth
def permission_manage(request):

    if request.method == "GET":

        username = request.session.get('user','')

        users = User.objects.all()

        permissions = UserPermission.objects.all()

        for user in users:

            if user.user_name == username:

                if user.permission_options == 1:

                    return render(request,"permission.html",
                                  {"username":username,
                                   "type":"list",
                                   "type_option":"permission_sap",
                                   "permissions":permissions})

                else:

                    return render(request,"permission.html",
                                  {"username":username,
                                   "type":"list",
                                   "permissions":permissions})

            else:

                return render(request,"permission.html",
                              {"username":username,
                               "type":"list",
                               "permissions":permissions})


@auth
def add_permission(request):

    '''创建权限'''

    permissions_name = UserPermission.objects.all()

    if request.method == "GET":

        return render(request,"permission_add.html",{"type":"add","permissions_name":permissions_name})
