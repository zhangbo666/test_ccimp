from django.shortcuts import render

from django.http import HttpResponseRedirect,JsonResponse

from ccimp_user_app.views import auth


from ccimp_permission_app.models.permissionClassModels import PermissionClass
from ccimp_user_app.models.userModels import User

from datetime import datetime, date,time,timedelta,timezone
from django.utils import timezone as timezonea
from django import utils

# import time


'''###############################################################################'''
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


'''###############################################################################'''
# 用户权限编辑
@auth
def edit_permission(request,uid):

    pass



'''###############################################################################'''
# 权限分类list
@auth
def permission_class(request):

    '''权限分类list'''


    tz_utc = timezone(timedelta(hours=8))

    print ("tz_utc-->",tz_utc)

    now1 = datetime.now()
    print ("now1-->",now1)

    now2 = now1.replace(tzinfo=tz_utc)

    print ("now2-->",now2)

    now3 = now2.strftime('%Y-%m-%d %H:%M:%S')

    print ("now3-->",now3)


    get_username = request.session.get('user', '')

    # permissionClasss = PermissionClass.objects.all()

    permissionClasss = PermissionClass.objects.filter(permission_options__gt='1')
    # permissionClasss = PermissionClass.objects.exclude(id=1)


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



'''###############################################################################'''

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

            now1 = datetime.now()
            now1 = datetime.today()

            now2 = now1.strftime('%Y-%m-%d %H:%M:%S')
            now2 = now2[11:13]
            now2 = int(now2)
            now3 = now1.replace(hour=now2+8)



            # tz_utc = timezone(timedelta(hours=8))
            #
            # now1 = datetime.now()
            #
            # now2 = now1.replace(tzinfo=tz_utc)
            #
            # now3 = now2.strftime('%Y-%m-%d %H:%M:%S')

            PermissionClass.objects.create(permission_chinese_name=pc_name,
                                           permission_english_name=pe_name,
                                           permission_options=po_name,
                                           create_time=now3)

            return HttpResponseRedirect("/permission/class/")

        else:

            return render(request, "permission_class_add.html", {"username": get_username,
                                                                 "type": "add",
                                                                 "type_option": "permission_sap",
                                                                 "po_name": "权限分类数据错误，请查看原因！"})



'''###############################################################################'''
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
                       "permissionclass":permissionclass})




'''###############################################################################'''
# 保存编辑权限分类
def save_permissionClass(request):

    '''保存编辑权限分类'''

    if request.method == "POST":

        pcname = request.POST.get("pcname","")
        pename = request.POST.get("pename", "")
        poname = request.POST.get("poname", "")
        pclass_id = request.POST.get("pclass_id","")

        print ("权限id-->",pclass_id)
        print ("pcname-->",pcname)
        print ("pename-->",pename)
        print ("poname-->",poname)

        permissionclass = PermissionClass.objects.get(id=pclass_id)

        if pcname == "":

            return JsonResponse({"status": 10101, "message": "权限名称为空！"})

        elif pename == "":

            return JsonResponse({"status": 10102, "message": "权限英文名为空！"})

        elif poname == "":

            return JsonResponse({"status": 10103, "message": "权限类型为空！"})

        if poname == "项目管理员" or poname == "模块管理员" or poname == "普通管理员":

            if poname == "项目管理员":

                poname = 2

            elif poname == "模块管理员":

                poname = 3

            elif poname == "普通管理员":

                poname = 4

            permissionclass.permission_chinese_name = pcname
            permissionclass.permission_english_name = pename
            permissionclass.permission_options      = poname

            permissionclass.save()

            return JsonResponse({"status": 10200, "message": "修改成功！"})

        else:

            return JsonResponse({"status": 10104, "message": "权限分类数据错误，请查看说明！"})




'''###############################################################################'''
@auth
#获取当前编辑页权限数据
def get_edit_permissionClass(request):

    if request.method == "POST":

        pclass_id = request.POST.get("pclass_id","")
        print ("权限id：",pclass_id)

        pclass_id = PermissionClass.objects.get(id=pclass_id)

        pcname = pclass_id.permission_chinese_name
        print (pcname)

        pename = pclass_id.permission_english_name
        print (pename)

        poname = pclass_id.permission_options
        print (poname)

        if poname == 2:

            poname = "项目管理员"

        elif poname == 3:

            poname = "模块管理员"

        elif poname == 4:

            poname = "普通管理员"


        return JsonResponse({"status": 10200, "message": "接口获取数据正确!","data":{"pcname":pcname,
                                                                                    "pename":pename,
                                                                                    "poname":poname}})







    # else:
    #
    #
    #         return JsonResponse({"status": 10100, "message": "方法请求错误!"})





