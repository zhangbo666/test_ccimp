from django.shortcuts import render

from django.http import HttpResponseRedirect,JsonResponse

from ccimp_user_app.views import auth

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from ccimp_permission_app.models.permissionClassModels import PermissionClass
from ccimp_user_app.models.userModels import User

# from datetime import datetime, date,time,timedelta,timezone
# from django.utils import timezone as timezonea
# from django import utils
# from time import strftime,localtime,time
# from dateutil import parser
from datetime import datetime
import time


'''###############################################################################'''
# 用户权限
@auth
def permission_manage(request):

    '''用户权限list'''

    if request.method == "GET":

        get_username = request.session.get('user','')

        # 查询全部数据
        users_all = User.objects.all()

        # 过滤掉permission_options=1的数据
        users = User.objects.filter(permission_options__gt='1')

        if not users:

             return render(request, "permission.html",
                     {"username": get_username,
                      "type": "list",
                      "type_option_admin": "permission_sap",
                      "aTag_":"0",
                      "error":"未找到数据，请查看原因！！！"})

        for user in users_all:

            # permission_options=1
            if user.permission_options == 1:

                if user.user_name == get_username:

                    paginator = Paginator(users,5)

                    # 最大分几页数字表示
                    paginator_num_pages = paginator.num_pages

                    # 分几页表示range(1, 3)，循环顺序1，2
                    paginator_num_pages_array_ = paginator.page_range

                    # 当前第一页表示<Page 1 of 2>
                    # 当前第二页表示<Page 2 of 2>
                    page1 = paginator.page(1)
                    page_num = page1.number

                    # 传一个页面数据get参数的值
                    page = request.GET.get('page','')
                    # print ("urlpage传参：",page)

                    try:

                        # 获取page参数的值
                        contacts = paginator.page(page)
                        # print ("contacts---------->1",contacts)

                    except PageNotAnInteger:

                        contacts = paginator.page(1)
                        # print ("contacts---------->2",contacts)

                    except EmptyPage:

                        contacts = paginator.page(paginator.num_pages)
                        # print ("contacts---------->3",contacts)

                    # print ("第二页索引：",contacts.number)

                    # print ("第几页：",contacts)


                    return render(request, "permission.html",
                                  {"type": "list",
                                   "type_option_admin": "permission_sap",
                                   "aTag_":"0",
                                   "username": get_username,
                                   "users": contacts,
                                   "page_num":page_num,
                                   "paginator_num_pages":paginator_num_pages,
                                   "paginator_num_pages_array_":paginator_num_pages_array_})

            else:

                return render(request, "404.html")


'''###############################################################################'''
# 用户权限编辑
@auth
def edit_permission(request,uid):

    '''用户权限编辑'''

    permission = User.objects.get(id=uid)

    get_username = request.session.get('user', '')

    if request.method == "GET":

        return render(request,"permission_edit.html",
                  {"username":get_username,
                   "type": "edit",
                   "type_option_admin": "permission_sap",
                   "aTag_":"0",
                   "permissionClasss": permission})


'''###############################################################################'''
# 用户权限搜索
@auth
def permission_search(request):

    '''用户权限搜索'''

    if request.method == "GET":

        get_username = request.session.get('user','')

        search_name = request.GET.get("search_name","")

        # 找到用户权限搜索数据:2个搜索条件以上过滤
        user_search_list = User.objects.filter(user_name__contains=search_name,permission_options__gt='1').order_by('id')#升序

        paginator = Paginator(user_search_list,5)

        # 最大分几页数字表示
        paginator_num_pages = paginator.num_pages
        # print ("共分：",str(paginator_num_pages)+"页")


        # 分几页表示range(1, 3)，循环顺序1，2
        paginator_num_pages_array_ = paginator.page_range
        # print ("数组形式表示：",paginator_num_pages_array_)

        # 当前第一页表示<Page 1 of 3>
        # 当前第二页表示<Page 2 of 3>
        # 当前第三页表示<Page 3 of 3>
        page1 = paginator.page(1)
        # print ("第一页：",page1)

        page_num = page1.number
        # print ("第一页：",page_num)


        if (len(user_search_list) == 0):

            return render(request,"permission.html",{"type":"list",
                                                     "type_option_admin": "permission_sap",
                                                     "aTag_":"0",
                                                     "username": get_username,
                                                     "users":user_search_list,
                                                     "search_error":"搜索查询结果为空，请重新查询！！！"})

        else:

            # 传一个页面数据get参数的值
            page = request.GET.get('page','')
            # print (page)

            try:

                # 获取page参数的值
                contacts = paginator.page(page)
                # print ("contacts---------->1",contacts)

            except PageNotAnInteger:

                contacts = paginator.page(1)

                # print ("contacts---------->2",contacts)

            except EmptyPage:

                contacts = paginator.page(paginator.num_pages)
                # print ("contacts---------->3",contacts)

            return render(request,"permission.html",{"type":"list",
                                                     "type_option_admin": "permission_sap",
                                                     "aTag_":"0",
                                                     "username": get_username,
                                                     "users":contacts,
                                                     "page_num":page_num,
                                                     "search_name":search_name,
                                                     "paginator_num_pages":paginator_num_pages,
                                                     "paginator_num_pages_array_":paginator_num_pages_array_})


'''###############################################################################'''
# 权限分类list
@auth
def permission_class(request):

    '''权限分类list'''

    get_username = request.session.get('user', '')

    permissionClasss = PermissionClass.objects.filter(permission_options__gt='1')
    # permissionClasss = PermissionClass.objects.exclude(id=1)

    paginator = Paginator(permissionClasss,5)

    # 最大分几页数字表示
    paginator_num_pages = paginator.num_pages
    # print ("共分：",str(paginator_num_pages)+"页")


    # 分几页表示range(1, 3)，循环顺序1，2
    paginator_num_pages_array_ = paginator.page_range
    # print ("数组形式表示：",paginator_num_pages_array_)

    # 当前第一页表示<Page 1 of 3>
    # 当前第二页表示<Page 2 of 3>
    # 当前第三页表示<Page 3 of 3>

    page1 = paginator.page(1)
    # print ("第一页：",page1)

    page_num = page1.number
    # print ("第一页：",page_num)

    # 传一个页面数据get参数的值
    page = request.GET.get('page','')
    # print (page)

    try:

        # 获取page参数的值
        contacts = paginator.page(page)
        # print ("contacts---------->1",contacts)

    except PageNotAnInteger:

        contacts = paginator.page(1)
        # print ("contacts---------->2",contacts)

    except EmptyPage:

        contacts = paginator.page(paginator.num_pages)
        # print ("contacts---------->3",contacts)

    if request.method == "GET":

        users_all = User.objects.all()

        if not permissionClasss:

             return render(request, "permission_class.html",
                     {"username": get_username,
                      "type": "list",
                      "type_option_admin": "permission_sap",
                      "aTag_":"0",
                      "error":"未找到数据，请查看原因！！！"})

        for user in users_all:

            if user.user_name == get_username:

                if user.permission_options == 1:

                    return render(request,"permission_class.html",
                                {"username":get_username,
                                 "type":"list",
                                 "type_option_admin":"permission_sap",
                                 "aTag_":"0",
                                 "permissionClasss":contacts,
                                 "page_num":page_num,
                                 "paginator_num_pages":paginator_num_pages,
                                 "paginator_num_pages_array_":paginator_num_pages_array_})

                else:

                    return render(request,"404.html")

    #添加页面返回时，触发post
    else:

        return render(request,"permission_class.html",
                      {"username":get_username,
                       "type": "list",
                       "type_option_admin":"permission_sap",
                       "aTag_":"0",
                       "permissionClasss": contacts,
                       "page_num":page_num,
                       "paginator_num_pages":paginator_num_pages,
                       "paginator_num_pages_array_":paginator_num_pages_array_})


'''###############################################################################'''

# 添加权限分类
@auth
def add_permissionClass(request):

    '''创建权限分类'''

    get_username = request.session.get('user', '')

    if request.method == "GET":

        user = User.objects.get(user_name=get_username)

        if user.user_name == get_username:

            if user.permission_options == 1:

                    return render(request,"permission_class_add.html",
                                  {"username":get_username,
                                   "type":"add",
                                   "type_option_admin":"permission_sap",
                                   "aTag_":"0"})

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
                                                                 "type_option_admin": "permission_sap",
                                                                 "aTag_":"0",
                                                                 "pc_name": "权限中文名称不能为空！"})
        elif pe_name == "":

            return render(request, "permission_class_add.html", {"username": get_username,
                                                                 "type": "add",
                                                                 "type_option_admin": "permission_sap",
                                                                 "aTag_":"0",
                                                                 "pe_name": "权限英文名称不能为空！"})

        elif po_name == "":

            return render(request, "permission_class_add.html", {"username": get_username,
                                                                 "type": "add",
                                                                 "type_option_admin": "permission_sap",
                                                                 "aTag_":"0",
                                                                 "po_name": "权限类别不能为空！"})

        if po_name == "项目管理员" or po_name == "普通管理员":

            if po_name == "项目管理员":

                po_name = 2

            elif po_name == "普通管理员":

                po_name = 3


            currery_now = datetime.utcfromtimestamp(time.time()+28800)
            # print ("currery_now-->",currery_now,type(currery_now))
            currery_now = currery_now.strftime('%Y-%m-%d %H:%M:%S')
            # print ("currery_now-->",currery_now,type(currery_now))

            PermissionClass.objects.create(permission_chinese_name=pc_name,
                                           permission_english_name=pe_name,
                                           permission_options=po_name,
                                           create_time=currery_now)

            return HttpResponseRedirect("/permission/class/")

        else:

            return render(request, "permission_class_add.html", {"username": get_username,
                                                                 "type": "add",
                                                                 "type_option_admin": "permission_sap",
                                                                 "aTag_":"0",
                                                                 "po_name": "权限类别数据错误，请查看原因！"})


'''###############################################################################'''
# 编辑权限分类
@auth
def edit_permissionClass(request,pclass_id):

    '''编辑权限分类'''

    get_username = request.session.get('user', '')

    if request.method == "GET":

        return render(request,"permission_class_edit.html",
                      {"username":get_username,
                       "type": "edit",
                       "type_option_admin":"permission_sap",
                       "aTag_":"0"})


'''###############################################################################'''
# 权限分类搜索
@auth
def permission_class_search(request):

    '''权限分类搜索'''

    if request.method == "GET":

        get_username = request.session.get('user','')

        search_name = request.GET.get("search_name","")

        # 找到权限分类搜索数据:2个搜索条件以上过滤
        permission_class_search_list = PermissionClass.objects.filter(permission_chinese_name__contains=search_name,permission_options__gt='1').order_by('id')#升序

        paginator = Paginator(permission_class_search_list,5)

        # 最大分几页数字表示
        paginator_num_pages = paginator.num_pages
        # print ("共分：",str(paginator_num_pages)+"页")


        # 分几页表示range(1, 3)，循环顺序1，2
        paginator_num_pages_array_ = paginator.page_range
        # print ("数组形式表示：",paginator_num_pages_array_)

        # 当前第一页表示<Page 1 of 3>
        # 当前第二页表示<Page 2 of 3>
        # 当前第三页表示<Page 3 of 3>

        page1 = paginator.page(1)
        # print ("第一页：",page1)

        page_num = page1.number
        # print ("第一页：",page_num)


        if (len(permission_class_search_list) == 0):

            return render(request,"permission_class.html",
                                  {"type":"list",
                                   "type_option_admin": "permission_sap",
                                   "aTag_":"0",
                                   "username": get_username,
                                   "permissionClasss":permission_class_search_list,
                                   "search_error":"搜索查询结果为空，请重新查询！！！"})

        else:

            # 传一个页面数据get参数的值
            page = request.GET.get('page','')
            # print (page)

            try:

                # 获取page参数的值
                contacts = paginator.page(page)
                # print ("contacts---------->1",contacts)

            except PageNotAnInteger:

                contacts = paginator.page(1)
                # print ("contacts---------->2",contacts)

            except EmptyPage:

                contacts = paginator.page(paginator.num_pages)

                # print ("contacts---------->3",contacts)

            return render(request,"permission_class.html",
                                    {"type":"list",
                                     "type_option_admin": "permission_sap",
                                     "aTag_":"0",
                                     "username": get_username,
                                     "permissionClasss":contacts,
                                     "page_num":page_num,
                                     "search_name":search_name,
                                     "paginator_num_pages":paginator_num_pages,
                                     "paginator_num_pages_array_":paginator_num_pages_array_})


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

            return JsonResponse({"status": 10103, "message": "权限类别为空！"})

        if poname == "项目管理员" or poname == "普通管理员":

            if poname == "项目管理员":

                poname = 2

            elif poname == "普通管理员":

                poname = 3

            # now1 = datetime.now()
            # # print ("now1-->>",now1)
            # # now1 = datetime.today()
            #
            # now_format = now1.strftime('%Y-%m-%d %H:%M:%S')
            # now_hour = now_format[11:13]
            # # print ("now_hour-->>",now_hour)
            # now_day = now_format[8:10]
            # # print ("now_day-->>",now_day)
            # now_hour = int(now_hour)
            # now_day = int(now_day)
            #
            # if now_hour == 16:
            #
            #     now_date = now1.replace(hour=0,day=now_day+1)
            #
            # elif now_hour == 17:
            #
            #     now_date = now1.replace(hour=1,day=now_day+1)
            #
            # elif now_hour == 18:
            #
            #     now_date = now1.replace(hour=2,day=now_day+1)
            #
            # elif now_hour == 19:
            #
            #     now_date = now1.replace(hour=3,day=now_day+1)
            #
            # elif now_hour == 20:
            #
            #     now_date = now1.replace(hour=4,day=now_day+1)
            #
            # elif now_hour == 21:
            #
            #     now_date = now1.replace(hour=5,day=now_day+1)
            #
            # elif now_hour == 22:
            #
            #     now_date = now1.replace(hour=6,day=now_day+1)
            #
            # elif now_hour == 23:
            #
            #     now_date = now1.replace(hour=7,day=now_day+1)
            #
            # else:
            #
            #     now_date = now1.replace(hour=now_hour+8)

            getCurreryEditDate = datetime.utcfromtimestamp(time.time()+28800)
            # print ("getCurreryEditDate-->",getCurreryEditDate,type(getCurreryEditDate))
            getCurreryEditDate_str = getCurreryEditDate.strftime('%Y-%m-%d %H:%M:%S')
            # print ("getCurreryEditDate_str-->",getCurreryEditDate_str,type(getCurreryEditDate_str))

            permissionclass.permission_chinese_name = pcname
            permissionclass.permission_english_name = pename
            permissionclass.permission_options      = poname
            permissionclass.update_time             = getCurreryEditDate_str

            permissionclass.save()

            return JsonResponse({"status": 10200, "message": "修改成功！"})

        else:

            return JsonResponse({"status": 10104, "message": "权限类别数据错误，请查看说明！"})




'''###############################################################################'''
#获取当前编辑页权限数据
def get_edit_permissionClass(request):

    if request.method == "POST":

        pclass_id = request.POST.get("pclass_id","")
        # print ("权限id：",pclass_id)

        pclass_id = PermissionClass.objects.get(id=pclass_id)

        pcname = pclass_id.permission_chinese_name
        # print (pcname)

        pename = pclass_id.permission_english_name
        # print (pename)

        poname = pclass_id.permission_options
        # print (poname)

        if poname == 2:

            poname = "项目管理员"

        elif poname == 3:

            poname = "普通管理员"


        return JsonResponse({"status": 10200, "message": "接口获取数据正确!","data":{"pcname":pcname,
                                                                                    "pename":pename,
                                                                                    "poname":poname}})
    else:

        return JsonResponse({"status": 10100, "message": "方法请求错误!"})



'''###############################################################################'''
#获取当前用户编辑页权限数据
@auth
def get_edit_permission(request):

    if request.method == "POST":

        pUser_id = request.POST.get("pUser_id","")
        # print ("用户id：",pUser_id)

        pUser_id = User.objects.get(id=pUser_id)

        pUser_name = pUser_id.user_name
        # print (pUser_name)

        pReal_name = pUser_id.real_name
        # print (pReal_name)

        pMail = pUser_id.mail
        # print (pMail)

        permission_option = pUser_id.permission_options
        # print (permission_option)


        if permission_option == 2:

            permission_option = "项目管理员"

        elif permission_option == 3:

            permission_option = "普通管理员"


        return JsonResponse({"status": 10200, "message": "接口获取数据正确!","data":{"pUser_name":pUser_name,
                                                                                  "pReal_name":pReal_name,
                                                                                  "pMail":pMail,
                                                                                  "permission_option":permission_option}})

    else:

        return JsonResponse({"status": 10100, "message": "方法请求错误!"})



'''###############################################################################'''
# 保存用户编辑权限分类
def save_permission(request):

    '''保存编辑权限分类'''

    if request.method == "POST":

        user_name = request.POST.get("user_name","")
        real_name = request.POST.get("real_name", "")
        mail = request.POST.get("mail", "")
        permission_options = request.POST.get("permission_options", "")
        pUser_id = request.POST.get("pUser_id","")

        # print ("用户id-->",pUser_id)
        # print ("user_name-->",user_name)
        # print ("real_name-->",real_name)
        # print ("mail-->",mail)
        # print ("permission_options-->",permission_options)


        permission = User.objects.get(id=pUser_id)

        if user_name == "":

            return JsonResponse({"status": 10101, "message": "用户账户为空！"})

        elif real_name == "":

            return JsonResponse({"status": 10102, "message": "用户中文名为空！"})

        elif mail == "":

            return JsonResponse({"status": 10103, "message": "用户邮件为空！"})

        elif permission_options == "":

            return JsonResponse({"status": 10104, "message": '权限类别为空！'})

        if permission_options == "项目管理员" or permission_options == "普通管理员":

            if permission_options == "项目管理员":

                permission_options = 2

            elif permission_options == "普通管理员":

                permission_options = 3

            # now1 = datetime.now()
            # # print ("now1-->>",now1)
            # # now1 = datetime.today()
            #
            # now_format = now1.strftime('%Y-%m-%d %H:%M:%S')
            # now_hour = now_format[11:13]
            # # print ("now_hour-->>",now_hour)
            # now_day = now_format[8:10]
            # # print ("now_day-->>",now_day)
            # now_hour = int(now_hour)
            # now_day = int(now_day)
            #
            # if now_hour == 16:
            #
            #     now_date = now1.replace(hour=0,day=now_day+1)
            #
            # elif now_hour == 17:
            #
            #     now_date = now1.replace(hour=1,day=now_day+1)
            #
            # elif now_hour == 18:
            #
            #     now_date = now1.replace(hour=2,day=now_day+1)
            #
            # elif now_hour == 19:
            #
            #     now_date = now1.replace(hour=3,day=now_day+1)
            #
            # elif now_hour == 20:
            #
            #     now_date = now1.replace(hour=4,day=now_day+1)
            #
            # elif now_hour == 21:
            #
            #     now_date = now1.replace(hour=5,day=now_day+1)
            #
            # elif now_hour == 22:
            #
            #     now_date = now1.replace(hour=6,day=now_day+1)
            #
            # elif now_hour == 23:
            #
            #     now_date = now1.replace(hour=7,day=now_day+1)
            #
            # else:
            #
            #     now_date = now1.replace(hour=now_hour+8)

            getCurreryEditDate = datetime.utcfromtimestamp(time.time()+28800)
            # print ("getCurreryEditDate-->",getCurreryEditDate,type(getCurreryEditDate))
            getCurreryEditDate_str = getCurreryEditDate.strftime('%Y-%m-%d %H:%M:%S')
            # print ("getCurreryEditDate_str-->",getCurreryEditDate_str,type(getCurreryEditDate_str))

            permission.user_name = user_name
            permission.real_name = real_name
            permission.mail = mail
            permission.permission_options = permission_options
            permission.update_time        = getCurreryEditDate_str

            permission.save()

            return JsonResponse({"status": 10200, "message": "修改成功！"})

        else:

            return JsonResponse({"status": 10105, "message": "权限类别数据错误，请查看说明！"})



