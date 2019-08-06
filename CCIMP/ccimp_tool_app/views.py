from django.shortcuts import render

from django.http import HttpResponseRedirect,JsonResponse,HttpResponse

from ccimp_user_app.views import auth

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from ccimp_permission_app.models.permissionClassModels import PermissionClass
from ccimp_user_app.models.userModels import User

from externalClass.publicKeyRsa import publicKeyRsa
from externalClass.userLogin import userLogin
from externalClass.getPackageDetail import getPackageDetail
from externalClass.getOrderInfo import getOrderInfo
from externalClass.adminLogin import adminLogin
from externalClass.processOrder import processOrder

from db_config.talkQueryUserOrder import talk_query_user_order_success
from db_config.db_config import *

import json


'''###############################################################################'''
#购买list
@auth
def sale_order(request):

    get_username = request.session.get('user','')

    users = User.objects.all()

    if request.method == "GET":

        for user in users:

            if user.user_name == get_username:

                if user.permission_options == 1:

                    return render(request,"tool_sale_order.html",
                                  {"username":get_username,
                                   "type_option_admin":"permission_sap"})

                elif user.permission_options == 2:

                    return render(request,"tool_sale_order.html",
                                  {"username":get_username})

                elif user.permission_options == 3:

                    return render(request,"tool_sale_order.html",
                                  {"username":get_username})

'''###############################################################################'''
#获取套餐详情
@auth
def get_package_detail(request):

    if request.method == "POST":

        user_mobile = request.POST.get("userMobile","")
        user_password = request.POST.get("userPasword","")

        # print ("user_mobile-->",user_mobile)
        # print ("user_password-->",user_password)

        if user_mobile == "":

            # return HttpResponse("用户手机号不能为空！")
            return JsonResponse({"status_code":10101,
                                 "message":"用户手机号不能为空！"})

        elif user_password == "":

            # return HttpResponse("用户密码不能为空！")
            return JsonResponse({"status_code":10102,
                                 "message":"用户密码不能为空！"})

        elif len(user_mobile)< 11 or len(user_mobile)>11:

            # return HttpResponse("用户手机号输入错误，请重新输入！")
            return JsonResponse({"status_code":10103,
                                 "message":"用户手机号输入错误，请重新输入！"})
        else:

            #调用获取加密密码接口
            pwd = publicKeyRsa(user_password)

            #调用获取登录状态接口
            req = userLogin(user_mobile,pwd)

            #调用获取套餐详情接口
            point_detail_list = getPackageDetail(req)

            #json转list
            point_detail_json = json.loads(point_detail_list)

            # print ("point_detail_json-->",point_detail_json)
            # print ("point_detail_json-->",type(point_detail_json))

            # for point_info in point_detail_json['data']:

                # print ("point_info-->",point_info)
                # print ("point_info-->",type(point_info))

                # pointDetail = {
                #
                #     "point_id":p_info['point_id'],
                #     "name":p_info['name'],
                #     "price":p_info['price'],
                #     "point_type":p_info['point_type'],
                # }

                # point_detail_list.append(pointDetail)

            point_info = point_detail_json['data']
            print ("point_info-->",point_info)
            print ("point_info-->",type(point_info))
            return JsonResponse({"status_code":10200,
                                 "message":"获取套餐数据正确！！！",
                                 "result":point_info})


'''###############################################################################'''
#下单成功
@auth
def order_pay_success(request):

    if request.method == "POST":

        user_mobile = request.POST.get("userMobile","")
        user_password = request.POST.get("userPasword","")
        point_id = request.POST.get("point_id","")

        if user_mobile == "":

            # return HttpResponse("用户手机号不能为空！")
            return JsonResponse({"status_code":10101,
                                 "message":"用户手机号不能为空！"})

        elif user_password == "":

            # return HttpResponse("用户密码不能为空！")
            return JsonResponse({"status_code":10102,
                                 "message":"用户密码不能为空！"})

        elif len(user_mobile)< 11 or len(user_mobile)>11:

            # return HttpResponse("用户手机号输入错误，请重新输入！")
            return JsonResponse({"status_code":10103,
                                 "message":"用户手机号输入错误，请重新输入！"})
        else:

            #调用获取加密密码接口
            pwd = publicKeyRsa(user_password)

            #调用获取登录状态接口
            req = userLogin(user_mobile,pwd)

            #调用获取套餐详情接口
            # point_detail_list = getPackageDetail(req)

            #获取用户下单详情
            status_flage = getOrderInfo(req,point_id)

            if status_flage == False:

                return JsonResponse({"status_code":10104,
                                     "message":"签名获取失败，不能创建订单数据！"})

            else:

                return JsonResponse({"status_code":10200,
                                     "message":"下单成功，数据返回正确！！！",
                                     "result":status_flage})


'''###############################################################################'''
#获取订单详情
@auth
def get_order_detail(request):

    if request.method == "POST":

        order_id = request.POST.get("order_id","")

        #调用获取加密密码接口
        # pwd = publicKeyRsa(user_password)

        #调用获取登录状态接口
        # req = userLogin(user_mobile,pwd)

        #调用获取套餐详情接口
        # point_detail_list = getPackageDetail(req)

        #获取用户下单详情
        # status_flage = getOrderInfo(req,point_id)

        #获取订单详情
        order_detail = talk_query_user_order_success(order_id)

        # cursor_talk.close()
        #
        # conn_talk.close()

        if order_detail == ():

            return JsonResponse({"status_code":10101,
                                 "message":"订单获取失败，无法读取该订单数据！"})

        else:

            return JsonResponse({"status_code":10200,
                                 "message":"订单获取正常！",
                                 "result":order_detail})


'''###############################################################################'''
#处理订单
@auth
def process_order(request):

    if request.method == "POST":

        order_id = request.POST.get("order_id","")

        # print ("order_id-->",type(order_id))


        if order_id == "":

            return JsonResponse({"status_code":10101,
                                 "message":"订单号为空，无法处理该订单数据！"})

        else:

            #调用admin后台登录接口
            req = adminLogin()

            #调用admin后台处理订单接口
            responses_result = processOrder(req,order_id)

            # print ("responses_result-->",responses_result)
            # print ("responses_result-->",type(responses_result))

            if responses_result.text == '订单处理成功':

                return JsonResponse({"status_code":10200,
                                     "message":responses_result.text})

            else:

                return JsonResponse({"status_code":10102,
                                     "message":"订单处理失败！"})


