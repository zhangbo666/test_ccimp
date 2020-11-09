
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

from django.shortcuts import render

from ccimp_user_app.views import auth

from ccimp_user_app.models.userModels import User

from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator

from ccimp_systemSettings_app.models.WebConfigModels import WebConfig

from django.db.models import Q

from datetime import datetime

import time


'''###############################################################################'''
# 系统配置文件链接
@auth
def systemConfig_manage(request):

    get_username = request.session.get('user','')

    users = User.objects.all()

    for user in users:

        webConfigs = WebConfig.objects.all()

        paginator = Paginator(webConfigs, 5)

        # 最大分几页数字表示
        paginator_num_pages = paginator.num_pages
        # print ("共分：",str(paginator_num_pages)+"页")

        # 分几页表示range(1, 4)，循环顺序1，2，3
        paginator_num_pages_array_ = paginator.page_range
        # print ("数组形式表示：",paginator_num_pages_array_)


        # 当前第一页表示<Page 1 of 2>
        # 当前第二页表示<Page 2 of 2>
        page1 = paginator.page(1)
        # print ("第一页：",page1)

        page_num = page1.number
        # print ("第一页：",page_num)

        # 传一个页面数据get参数的值
        page = request.GET.get('page', '')
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

        if user.user_name == get_username:

            if user.permission_options == 1:

                if not webConfigs:

                    return render(request, "systemConfig.html",
                                  {"username": get_username,
                                   "type": "list",
                                   "type_option_admin": "permission_sap",
                                   "aTag_": "4",
                                   "not_webConfigs_data": "当前系统配置文件为空！"})

                else:

                    return render(request,"systemConfig.html",
                                  {"username":get_username,
                                   "type_option_admin":"permission_sap",
                                   "aTag_":"4",
                                   "type":"list",
                                   "webConfigs": contacts,
                                   "page_num": page_num,
                                   "paginator_num_pages": paginator_num_pages,
                                   "paginator_num_pages_array_": paginator_num_pages_array_})

            else:

                return render(request, "404.html")


'''###############################################################################'''
# 创建系统配置文件
def add_webConfigs(request):

    '''创建系统配置文件'''

    get_username = request.session.get('user', '')

    if request.method == "GET":

        user = User.objects.get(user_name=get_username)

        if user.user_name == get_username:

            if user.permission_options == 1:

                return render(request, "systemConfig_add.html",
                              {"username": get_username,
                               "type_option_admin": "permission_sap",
                               "aTag_": "4",
                               "type": "add"})

            else:

                return render(request,"404.html")

        else:

            pass

    else:

        webConfig_name = request.POST.get("webConfig_name", "")
        webConfig_key = request.POST.get("webConfig_key", "")
        webConfig_value = request.POST.get("webConfig_value", "")
        webConfig_describe = request.POST.get("webConfig_describe", "")

        user = User.objects.get(user_name=get_username)

        if user.user_name == get_username:

            if user.permission_options == 1:

                if webConfig_name == "":

                    return render(request,"systemConfig_add.html",
                                  {"username":get_username,
                                   "type":"add",
                                   "type_option_admin":"permission_sap",
                                   "aTag_":"4",
                                   "webConfig_name": "配置名称不能为空！"})

                elif webConfig_key == "":

                    return render(request, "systemConfig_add.html",
                                  {"username": get_username,
                                   "type": "add",
                                   "type_option_admin": "permission_sap",
                                   "aTag_": "4",
                                   "webConfig_key": "配置key不能为空！"})

                elif webConfig_value == "":

                    return render(request, "systemConfig_add.html",
                                  {"username": get_username,
                                   "type": "add",
                                   "type_option_admin": "permission_sap",
                                   "aTag_": "4",
                                   "webConfig_value": "配置value不能为空！"})

            else:

                return render(request, "404.html")

            currery_now = datetime.utcfromtimestamp(time.time()+28800)
            # print ("currery_now-->",currery_now,type(currery_now))
            currery_now = currery_now.strftime('%Y-%m-%d %H:%M:%S')
            # print ("currery_now-->",currery_now,type(currery_now))

            WebConfig.objects.create(nameConfig=webConfig_name,
                                     keyConfig=webConfig_key,
                                     valueConfig=webConfig_value,
                                     describeConfig=webConfig_describe,
                                     create_time=currery_now)

            return HttpResponseRedirect("/systemSettings/Admin/webConfig")


        else:

            pass


'''###############################################################################'''
# 编辑系统配置文件
def edit_webConfigs(request,wCid):

    '''编辑系统配置文件'''

    get_username = request.session.get('user', '')

    if request.method == "GET":

        user = User.objects.get(user_name=get_username)

        if user.user_name == get_username:

            if user.permission_options == 1:

                return render(request,"systemConfig_edit.html",
                              {"username":get_username,
                               "type":"edit",
                               "type_option_admin":"permission_sap",
                               "aTag_":"4"})

            else:

                return render(request, "404.html")


'''###############################################################################'''
# 获取编辑项目数据
def get_edit_webConfig_data(request):

    '''获取编辑配置文件数据'''

    if request.method == "GET":

        ws_id = request.GET.get("ws_id","")

        WebConfigs = WebConfig.objects.get(id=ws_id)

        if ws_id == "":

            return JsonResponse({"status":10100,"message":"配置文件id为空！"})

        ws_nameConfig = WebConfigs.nameConfig
        ws_keyConfig  = WebConfigs.keyConfig
        ws_valueConfig = WebConfigs.valueConfig
        ws_describeConfig = WebConfigs.describeConfig

        return JsonResponse({"status": 10200, "message": "接口获取数据正确！","data":{"ws_nameConfig":ws_nameConfig,
                                                                                  "ws_keyConfig":ws_keyConfig,
                                                                                  "ws_valueConfig":ws_valueConfig,
                                                                                  "ws_describeConfig":ws_describeConfig}})
    else:

        return JsonResponse({"status": 10101, "message": "方法请求错误！"})



'''###############################################################################'''
# 修改保存配置文件数据
def edit_save_webConfig(request):

    '''修改保存配置文件数据'''

    if request.method == "POST":

        wsId = request.POST.get("wsId","")
        webConfigName = request.POST.get("webConfigName","")
        webConfigKey = request.POST.get("webConfigKey", "")
        webConfigValue = request.POST.get("webConfigValue", "")
        webConfigDescribe = request.POST.get("webConfigDescribe","")

        webConfig = WebConfig.objects.get(id=wsId)

        if webConfigName == "":

            return JsonResponse({"status": 10101, "message": "配置文件名称为空！"})

        elif webConfigKey == "":

            return JsonResponse({"status": 10102, "message": "配置文件Key为空！"})

        elif webConfigValue == "":

            return JsonResponse({"status": 10103, "message": "配置文件value为空！"})


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

        webConfig.nameConfig     = webConfigName
        webConfig.keyConfig      = webConfigKey
        webConfig.valueConfig    = webConfigValue
        webConfig.describeConfig = webConfigDescribe
        webConfig.update_time    = getCurreryEditDate_str

        webConfig.save()

        return JsonResponse({"status": 10200, "message": "修改成功！"})


'''###############################################################################'''
# 配置文件搜索
def webConfig_search(request):

    '''配置文件搜索'''

    get_username = request.session.get('user','')

    if request.method == "GET":

        users = User.objects.all()

        for user in users:

            search_name = request.GET.get("search_name","")
            search_key = request.GET.get("search_key","")
            # print (search_name)
            # print (search_key)

            #or关系
            # webConfig_search_list = WebConfig.objects.filter(Q(nameConfig__contains=search_name) | Q(keyConfig__contains=search_key))

            #and关系
            webConfig_search_list = WebConfig.objects.filter(nameConfig__contains=search_name,keyConfig__contains=search_key).order_by('id')#升序

            paginator = Paginator(webConfig_search_list,5)

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

            if user.user_name == get_username:

                if user.permission_options == 1:

                    if not webConfig_search_list:

                        return render(request,"systemConfig.html",
                                  {"username":get_username,
                                   "type":"list",
                                   "type_option_admin":"permission_sap",
                                   "aTag_":"4",
                                   "webConfigs_data_search_error":"搜索系统配置文件查询结果为空，请重新查询！"})

                    else:

                        return render(request,"systemConfig.html",
                                      {"username":get_username,
                                       "type":"list",
                                       "type_option_admin":"permission_sap",
                                       "aTag_":"4",
                                       "webConfigs":contacts,
                                       "page_num":page_num,
                                       "paginator_num_pages":paginator_num_pages,
                                       "paginator_num_pages_array_":paginator_num_pages_array_,
                                       "search_name":search_name,
                                       "search_key":search_key})

                else:

                    return render(request,"404.html")