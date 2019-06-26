#!/usr/bin/python
#encoding:utf-8


__author__ = 'zhangbo'

from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# from ccimp_project_app.models.projectModels import Project
from ccimp_user_app.models.userModels import User
from ccimp_permission_app.models.permissionClassModels import PermissionClass

# from datetime import datetime

# from project_app.forms import ProjectForm

from ccimp_user_app.views import auth


# 登录成功，默认项目管理页
@auth
def project_manage(request):

    if request.method == "GET":

        username = request.session.get('user','')

        users = User.objects.all()

        permissionClasss = PermissionClass.objects.all()

        for user in users:

            if user.user_name == username:

                if user.permission_options == 1:

                    return render(request,"project.html",
                                  {"username":username,
                                   "type":"list",
                                   "type_option":"permission_sap",
                                   "permissionClasss":permissionClasss})

                else:

                    print (12321)

                    return render(request,"project.html",{"username":username})

    # project_all = Project.objects.all()
    #
    # paginator = Paginator(project_all,5)
    #
    # # 最大分几页数字表示
    # paginator_num_pages = paginator.num_pages
    # print ("共分：",str(paginator_num_pages)+"页")
    #
    # # 分几页表示range(1, 3)，循环顺序1，2
    # paginator_num_pages_array_ = paginator.page_range
    # print ("数组形式表示：",paginator_num_pages_array_)
    #
    #
    # # 当前第一页表示<Page 1 of 2>
    # # 当前第二页表示<Page 2 of 2>
    # page1 = paginator.page(1)
    # print ("第一页：",page1)
    #
    # page_num = page1.number
    # print ("第一页：",page_num)
    #
    #
    # # 传一个页面数据get参数的值
    # page = request.GET.get('page','')
    # print ("urlpage传参：",page)
    #
    #
    # try:
    #
    #     # 获取page参数的值
    #     contacts = paginator.page(page)
    #     print ("contacts---------->1",contacts)
    #
    # except PageNotAnInteger:
    #
    #     contacts = paginator.page(1)
    #
    #     print ("contacts---------->2",contacts)
    #
    # except EmptyPage:
    #
    #     contacts = paginator.page(paginator.num_pages)
    #
    #     print ("contacts---------->3",contacts)
    #
    # print ("第二页索引：",contacts.number)
    #
    # print ("第几页：",contacts)
    #
    #
    # return render(request,"project.html",{"projects":contacts,
    #                                       "type":"list",
    #                                       "page":page,
    #                                       "page_num":page_num,
    #                                       "paginator_num_pages":paginator_num_pages,
    #                                       "paginator_num_pages_array_":paginator_num_pages_array_})
