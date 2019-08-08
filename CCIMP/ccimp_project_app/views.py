#!/usr/bin/python
#encoding:utf-8


__author__ = 'zhangbo'

from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

from django.shortcuts import render

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from ccimp_project_app.models.projectModels import Project
from ccimp_user_app.models.userModels import User
from ccimp_permission_app.models.permissionClassModels import PermissionClass
from ccimp_user_app.views import auth

from datetime import datetime
import time

'''###############################################################################'''
# 登录成功，默认项目管理页
@auth
def project_manage(request):

    '''登录成功，默认项目管理页'''

    get_username = request.session.get('user','')

    # modules  = Module.objects.all()

    # if request.method == "GET":

    users = User.objects.all()

    for user in users:

        projects = Project.objects.filter(user_id=user.id)

        paginator = Paginator(projects,5)

        # 最大分几页数字表示
        paginator_num_pages = paginator.num_pages
        print ("共分：",str(paginator_num_pages)+"页")

        # 分几页表示range(1, 4)，循环顺序1，2，3
        paginator_num_pages_array_ = paginator.page_range
        print ("数组形式表示：",paginator_num_pages_array_)


        # 当前第一页表示<Page 1 of 2>
        # 当前第二页表示<Page 2 of 2>
        page1 = paginator.page(1)
        print ("第一页：",page1)

        page_num = page1.number
        print ("第一页：",page_num)

        # 传一个页面数据get参数的值
        page = request.GET.get('page','')
        print ("urlpage传参：",page)

        try:

            # 获取page参数的值
            contacts = paginator.page(page)
            print ("contacts---------->1",contacts)

        except PageNotAnInteger:

            contacts = paginator.page(1)

            print ("contacts---------->2",contacts)

        except EmptyPage:

            contacts = paginator.page(paginator.num_pages)

            print ("contacts---------->3",contacts)

        if user.user_name == get_username:

            if user.permission_options == 1:

                if not projects:

                    return render(request,"project_list.html",
                              {"username":get_username,
                               "type":"list",
                               "type_option_admin":"permission_sap",
                               "type_option_project":"permission_sap_pp",
                               "not_projects_data":"当前账户未创建项目！"})

                else:

                    return render(request,"project_list.html",
                                  {"username":get_username,
                                   "type":"list",
                                   "type_option_admin":"permission_sap",
                                   "type_option_project":"permission_sap_pp",
                                   "projects":contacts,
                                   "page_num":page_num,
                                   "paginator_num_pages":paginator_num_pages,
                                   "paginator_num_pages_array_":paginator_num_pages_array_})


            elif user.permission_options == 2:

                if not projects:

                    return render(request,"project_list.html",
                                  {"username":get_username,
                                   "type":"list",
                                   "type_option_project":"permission_sap_pp",
                                   "not_projects_data":"当前账户未创建项目！"})

                else:

                    return render(request,"project_list.html",
                                  {"username":get_username,
                                   "type":"list",
                                   "type_option_project":"permission_sap_pp",
                                   "projects":contacts,
                                   "page_num":page_num,
                                   "paginator_num_pages":paginator_num_pages,
                                   "paginator_num_pages_array_":paginator_num_pages_array_})

            elif user.permission_options == 3:

                return render(request,"module_list.html",
                              {"username":get_username,
                               "type":"list",
                               "type_option":"permission_gp",
                               "modules":"modules"})

            else:

                return render(request,"404.html")


    #添加页面返回时，触发post
    # else:
    #
    #     users = User.objects.all()
    #
    #     for user in users:
    #
    #         projects = Project.objects.filter(user_id=user.id)
    #
    #         print ("projects-->",projects)
    #
    #         if user.user_name == get_username:
    #
    #             if user.permission_options == 1:
    #
    #                 return render(request,"project_list.html",
    #                               {"username":get_username,
    #                                "type":"list",
    #                                "type_option_admin":"permission_sap",
    #                                "type_option_project":"permission_sap_pp",
    #                                "projects":projects})
    #
    #             elif user.permission_options == 2:
    #
    #                 return render(request,"project_list.html",
    #                               {"username":get_username,
    #                                "type":"list",
    #                                "type_option_project":"permission_sap_pp",
    #                                "projects":projects})
    #
    #             elif user.permission_options == 3:
    #
    #                 return render(request,"module_list.html",
    #                               {"username":get_username,
    #                                "type":"list",
    #                                "type_option":"permission_gp",
    #                                "modules":"modules"})
    #
    #             else:
    #
    #                 return render(request,"404.html")

        # return render(request,"project_list.html",
        #               {"username":get_username,
        #                "type": "list",
        #                "type_option":"permission_sap",
        #                "type_option_admin":"permission_sap_pp",
        #                "projects":projects,
        #                "page_num":page_num,
        #                "permissionClasss": contacts,
        #                "paginator_num_pages":paginator_num_pages,
        #                "paginator_num_pages_array_":paginator_num_pages_array_
        #                })



'''###############################################################################'''
# 创建项目
def add_project(request):

    '''创建项目'''

    get_username = request.session.get('user', '')

    if request.method == "GET":

        user = User.objects.get(user_name=get_username)

        if user.user_name == get_username:

            if user.permission_options == 1:

                    return render(request,"project_add.html",
                                  {"username":get_username,
                                   "type":"add",
                                   "type_option_admin":"permission_sap",
                                   "type_option_project":"permission_sap_pp",})

            elif user.permission_options == 2:

                    return render(request,"project_add.html",
                                  {"username":get_username,
                                   "type":"add",
                                   "type_option_project":"permission_sap_pp"})

            else:


                return render(request,"404.html")

        else:

            pass

    else:

        project_name = request.POST.get("project_name", "")
        project_describe = request.POST.get("project_describe", "")
        # project_status = request.POST.get("project_status", "")

        user = User.objects.get(user_name=get_username)

        if user.user_name == get_username:

            if user.permission_options == 1:

                if project_name == "":

                    return render(request,"project_add.html",
                                  {"username":get_username,
                                   "type":"add",
                                   "type_option_admin":"permission_sap",
                                   "type_option_project":"permission_sap_pp",
                                   "project_name": "项目名称不能为空！"})

                # elif project_status == "请选择：":
                #
                #     return render(request,"project_add.html",
                #                   {"username":get_username,
                #                    "type":"add",
                #                    "type_option_admin":"permission_sap",
                #                    "type_option_project":"permission_sap_pp",
                #                    "project_status": "项目状态不能为空！"})

            elif user.permission_options == 2:

                if project_name == "":

                    return render(request,"project_add.html",
                                  {"username":get_username,
                                   "type":"add",
                                   "type_option_project":"permission_sap_pp",
                                   "project_name": "项目名称不能为空！"})

                # elif project_status == "请选择：":
                #
                #     return render(request,"project_add.html",
                #                   {"username":get_username,
                #                    "type":"add",
                #                    "type_option_project":"permission_sap_pp",
                #                    "project_status": "项目状态不能为空！"})

            # if project_status == "禁用":
            #
            #     project_status = 0
            #
            # elif project_status == "开启":
            #
            #     project_status = 1
            #
            # elif project_status == "进行中":
            #
            #     project_status = 2
            #
            # elif project_status == "已完成":
            #
            #     project_status  = 3
            #
            # elif project_status == "暂停":
            #
            #      project_status = 4

            currery_now = datetime.utcfromtimestamp(time.time()+28800)
            # print ("currery_now-->",currery_now,type(currery_now))
            currery_now = currery_now.strftime('%Y-%m-%d %H:%M:%S')
            # print ("currery_now-->",currery_now,type(currery_now))

            Project.objects.create(user_id=user.id,
                                   name=project_name,
                                   describe=project_describe,
                                   create_time=currery_now)

            return HttpResponseRedirect("/project/")


        else:

            pass



        # else:
        #
        #     return render(request, "permission_class_add.html", {"username": get_username,
        #                                                          "type": "add",
        #                                                          "type_option": "permission_sap",
        #                                                          "po_name": "权限类别数据错误，请查看原因！"})


'''###############################################################################'''
# 编辑项目
def edit_project(request,pid):

    '''编辑项目'''

    get_username = request.session.get('user', '')

    if request.method == "GET":

        user = User.objects.get(user_name=get_username)

        if user.user_name == get_username:

            if user.permission_options == 1:

                return render(request,"project_edit.html",
                              {"username":get_username,
                               "type":"edit",
                               "type_option_admin":"permission_sap",
                               "type_option_project":"permission_sap_pp"})

            elif user.permission_options == 2:

                return render(request,"project_edit.html",
                              {"username":get_username,
                               "type":"edit",
                               "type_option_project":"permission_sap_pp"})


'''###############################################################################'''
# 获取编辑项目数据
def get_edit_project_data(request):

    '''获取编辑项目数据'''

    if request.method == "POST":

        pclass_id = request.POST.get("pclass_id","")

        projects = Project.objects.get(id=pclass_id)

        if pclass_id == "":

            return JsonResponse({"status":10100,"message":"项目id为空！"})

        p_name = projects.name
        p_status = projects.status
        p_describe = projects.describe

        if p_status == 0:

            p_status = "禁用"

        elif p_status == 1:

            p_status = "开启"

        elif p_status == 2:

            p_status = "进行中"

        elif p_status == 3:

            p_status = "已完成"

        elif p_status == 4:

            p_status = "暂停"

        return JsonResponse({"status": 10200, "message": "接口获取数据正确！","data":{"p_name":p_name,
                                                                                  "p_status":p_status,
                                                                                  "p_describe":p_describe}})
    else:

        return JsonResponse({"status": 10101, "message": "方法请求错误！"})




'''###############################################################################'''
# 修改保存项目数据
def edit_save_project(request):

    '''修改保存项目数据'''

    if request.method == "POST":

        projectName = request.POST.get("projectName","")
        projectStatus = request.POST.get("projectStatus", "")
        projectDescribe = request.POST.get("projectDescribe", "")
        pclass_id = request.POST.get("pclass_id","")

        # print ("项目名称-->",projectName)
        # print ("项目状态-->",projectStatus,type(projectStatus))
        # print ("项目描述-->",projectDescribe)
        # print ("项目id-->",pclass_id)


        project = Project.objects.get(id=pclass_id)

        if projectName == "":

            return JsonResponse({"status": 10101, "message": "项目名称为空！"})

        elif projectStatus == "请选择：":

            return JsonResponse({"status": 10102, "message": "项目状态选择错误！"})

        if projectStatus == "禁用":

            projectStatus = 0

        elif projectStatus == "开启":

            projectStatus = 1

        elif projectStatus == "进行中":

            projectStatus = 2

        elif projectStatus == "已完成":

            projectStatus = 3

        elif projectStatus == "暂停":

            projectStatus = 4

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
        print ("getCurreryEditDate-->",getCurreryEditDate,type(getCurreryEditDate))
        getCurreryEditDate_str = getCurreryEditDate.strftime('%Y-%m-%d %H:%M:%S')
        print ("getCurreryEditDate_str-->",getCurreryEditDate_str,type(getCurreryEditDate_str))

        project.name        = projectName
        project.status      = projectStatus
        project.describe    = projectDescribe
        project.update_time = getCurreryEditDate_str

        project.save()

        return JsonResponse({"status": 10200, "message": "修改成功！"})


'''###############################################################################'''
# 项目删除
def delete_project(request,pid):

    '''项目删除'''

    if request.method == "GET":

        try:

            project = Project.objects.get(id=pid)

            project.delete()

        except Project.DoesNotExist:

            return HttpResponseRedirect("/project/")

        return HttpResponseRedirect("/project/")

    else:

        return HttpResponseRedirect("/project/")


'''###############################################################################'''
# 项目搜索
def project_search(request):

    '''项目搜索'''

    get_username = request.session.get('user','')

    if request.method == "GET":

        users = User.objects.all()

        for user in users:

            search_name = request.GET.get("search_name","")

            project_search_list = Project.objects.filter(name__contains=search_name,user_id=user.id).order_by('id')#升序

            paginator = Paginator(project_search_list,5)

            # 最大分几页数字表示
            paginator_num_pages = paginator.num_pages
            print ("共分：",str(paginator_num_pages)+"页")


            # 分几页表示range(1, 3)，循环顺序1，2
            paginator_num_pages_array_ = paginator.page_range
            print ("数组形式表示：",paginator_num_pages_array_)

            # 当前第一页表示<Page 1 of 3>
            # 当前第二页表示<Page 2 of 3>
            # 当前第三页表示<Page 3 of 3>

            page1 = paginator.page(1)
            print ("第一页：",page1)

            page_num = page1.number
            print ("第一页：",page_num)

            # 传一个页面数据get参数的值
            page = request.GET.get('page','')
            print (page)

            try:

                # 获取page参数的值
                contacts = paginator.page(page)
                print ("contacts---------->1",contacts)

            except PageNotAnInteger:

                contacts = paginator.page(1)

                print ("contacts---------->2",contacts)

            except EmptyPage:

                contacts = paginator.page(paginator.num_pages)

                print ("contacts---------->3",contacts)

            if user.user_name == get_username:

                if user.permission_options == 1:

                    if not project_search_list:

                        return render(request,"project_list.html",
                                  {"username":get_username,
                                   "type":"list",
                                   "type_option_admin":"permission_sap",
                                   "type_option_project":"permission_sap_pp",
                                   "not_projects_data":"搜索项目查询结果为空，请重新查询！"})

                    else:

                        return render(request,"project_list.html",
                                      {"username":get_username,
                                       "type":"list",
                                       "type_option_admin":"permission_sap",
                                       "type_option_project":"permission_sap_pp",
                                       "projects":contacts,
                                       "page_num":page_num,
                                       "paginator_num_pages":paginator_num_pages,
                                       "paginator_num_pages_array_":paginator_num_pages_array_})


                elif user.permission_options == 2:

                    if not project_search_list:

                        return render(request,"project_list.html",
                                      {"username":get_username,
                                       "type":"list",
                                       "type_option_project":"permission_sap_pp",
                                       "not_projects_data":"搜索项目查询结果为空，请重新查询！！"})

                    else:

                        return render(request,"project_list.html",
                                      {"username":get_username,
                                       "type":"list",
                                       "type_option_project":"permission_sap_pp",
                                       "projects":contacts,
                                       "page_num":page_num,
                                       "paginator_num_pages":paginator_num_pages,
                                       "paginator_num_pages_array_":paginator_num_pages_array_})

                elif user.permission_options == 3:

                    return render(request,"module_list.html",
                                  {"username":get_username,
                                   "type":"list",
                                   "type_option":"permission_gp",
                                   "modules":"modules"})

                else:

                    return render(request,"404.html")