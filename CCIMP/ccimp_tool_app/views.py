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

import json


'''###############################################################################'''
#购买list
@auth
def sale_order(request):

    get_username = request.session.get('user','')

    if request.method == "GET":

        return render(request,"tool_sale_order.html",
                      {"username":get_username,
                       "type_option":"permission_sap"})


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
            print (type(point_info))
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