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
from externalClass.public_configure import global_configure
from externalClass.getCheckCartInfo import getCheckCartInfo
from externalClass.getUserRole import getUserRole

from db_config.talkQueryUserOrder import talk_query_user_order_success
from db_config.talkQueryUserInfo import talk_query_user_info_detail_success
from db_config.talkQueryUserInfo import talk_query_user_info_id_success
from db_config.talkQueryUserWealth import talk_query_stu_point_user_wealth_success
from db_config.talkQueryUserWealth import talk_query_user_assets_enable_user_wealth_success
from db_config.talkQueryUserWealth import talk_query_user_assets_disable_point_user_wealth_success
from db_config.talkQueryUserWealth import talk_query_user_assets_disable_classtime_user_wealth_success
from db_config.talkQueryUserOrder import talk_query_user_order2_success
from db_config.talkQueryUserWealth import talk_query_user_assets_disable_na_pri_user_wealth_success
from db_config.talkQueryUserWealth import talk_query_user_assets_disable_na_open_user_wealth_success

from db_config.db_config import *

import json


'''###############################################################################'''
#售卖下单manage
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

            #登录错误或者不是内部网络
            if req == global_configure.login_error_message:

                return JsonResponse({"status_code":10100,
                     "message":req})

            else:

                #获取用户user_id
                user_id = talk_query_user_info_id_success(user_mobile)

                #获取用户身份
                user_role_info = getUserRole(user_id)
                # print (user_role_info)
                # print (type(user_role_info))

                if user_role_info == 12:

                    # return HttpResponse("该账户为美小用户，暂不支持套餐查询！")
                    return JsonResponse({"status_code":10105,
                                     "message":"该账户为美小用户，暂不支持套餐查询！"})


                #调用获取套餐详情接口
                point_detail_dict_jsonStr = getPackageDetail(req,user_role_info)

                #转为dict格式
                point_detail_dict = json.loads(point_detail_dict_jsonStr)
                # print ("point_detail_dict-->",point_detail_dict)
                # print ("point_detail_dict-->",type(point_detail_dict))

                #转为list格式
                point_info = point_detail_dict['data']
                # print ("point_info-->",point_info)
                # print ("point_info-->",type(point_info))
                # print (" ")

                user_role_info = point_detail_dict['userRole']
                # print ("user_role_info-->",user_role_info)
                # print ("user_role_info-->",type(user_role_info))
                # print (" ")

                #获取套餐数据为空
                if (point_info == []):

                    return JsonResponse({"status_code":10104,
                                         "message":"获取套餐数据为空，请查看原因！！！",
                                         "result":point_info,
                                         "user_role":user_role_info})
                else:

                    return JsonResponse({"status_code":10200,
                                         "message":"获取套餐数据正确！！！",
                                         "result":point_info,
                                         "user_role":user_role_info})


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

            #查看套餐是否可以被下单
            req_s = getCheckCartInfo(req,point_id)

            if req_s == False:

                return JsonResponse({"status_code":10104,
                                     "message":"您当前还有同类型未完成的课程，请上完课后再来购买！！！"})

            else:

                #获取用户下单详情
                status_flage = getOrderInfo(req,point_id)

                if status_flage == False:

                    return JsonResponse({"status_code":10105,
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

        #获取订单详情
        order_detail = talk_query_user_order_success(order_id)

        # cursor_talk.close()
        # conn_talk.close()

        if order_detail == ():

            return JsonResponse({"status_code":10101,
                                 "message":"订单获取失败，无法读取该订单数据！！！"})

        else:

            return JsonResponse({"status_code":10200,
                                 "message":"订单获取正常！！！",
                                 "result":order_detail})


'''###############################################################################'''
#处理订单
@auth
def process_order(request):

    if request.method == "POST":

        order_id = request.POST.get("order_id","")

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


'''###############################################################################'''
#学员信息manage
@auth
def user_info(request):

    get_username = request.session.get('user','')

    users = User.objects.all()

    if request.method == "GET":

        for user in users:

            if user.user_name == get_username:

                if user.permission_options == 1:

                    return render(request,"tool_user_info.html",
                                  {"username":get_username,
                                   "type_option_admin":"permission_sap"})

                elif user.permission_options == 2:

                    return render(request,"tool_user_info.html",
                                  {"username":get_username})

                elif user.permission_options == 3:

                    return render(request,"tool_user_info.html",
                                  {"username":get_username})


'''###############################################################################'''
#获取用户信息详情
@auth
def get_userinfo_detail(request):

    if request.method == "POST":

        user_detail_dict = {}

        disable_wealth_list_result = []

        disable_wealth_dict_result = {}

        user_mobile = request.POST.get("userMobile","")

        if user_mobile == "":

            # return HttpResponse("用户手机号不能为空！")
            return JsonResponse({"status_code":10101,
                                 "message":"用户手机号不能为空！"})

        elif len(user_mobile)< 11 or len(user_mobile)>11:

            # return HttpResponse("用户手机号输入错误，请重新输入！")
            return JsonResponse({"status_code":10102,
                                 "message":"用户手机号输入错误，请重新输入！"})
        else:

            #获取用户信息详情
            user_list_result = talk_query_user_info_detail_success(user_mobile)
            # print ("user_list_result-->",user_list_result)
            # print ("user_list_result-->",type(user_list_result))

            # cursor_talk.close()
            # conn_talk.close()

            if user_list_result == ():

                return JsonResponse({"status_code":10103,
                                     "message":"获取该用户信息失败！！！"})

            else:

                user_id = talk_query_user_info_id_success(user_mobile)
                # print ("user_id-->",user_id)
                # print ("user_id-->",type(user_id))

                #获取用户身份
                user_role_info = getUserRole(user_id)
                # print (user_role_info)
                # print (type(user_role_info))

				#获取用户身份失败或当前网络不是测试环境
                if user_role_info == global_configure.login_error_message:

                    return JsonResponse({"status_code":10104,
                                         "message":user_role_info})

                elif user_role_info == global_configure.query_role_message:

                    return JsonResponse({"status_code":10105,
                                         "message":user_role_info})

                #获取用户当前财富
                enable_wealth_list_result = talk_query_user_assets_enable_user_wealth_success(user_id)
                # print ("enable_wealth_list_result-->",enable_wealth_list_result)
                # print ("enable_wealth_list_result-->",type(enable_wealth_list_result))

                if (str(user_role_info) == "11" or str(user_role_info) == "14"):

                    #获取用户未开启次卡财富
                    disable_point_wealth_dict_result = talk_query_user_assets_disable_point_user_wealth_success(user_id)
                    # print ("disable_point_wealth_dict_result-->",disable_point_wealth_dict_result)
                    # print ("disable_point_wealth_dict_result-->",type(disable_point_wealth_dict_result))

                    #获取用户未开启课时财富
                    disable_classtime_wealth_dict_result = talk_query_user_assets_disable_classtime_user_wealth_success(user_id)
                    # print ("disable_classtime_wealth_dict_result-->",disable_classtime_wealth_dict_result)
                    # print ("disable_classtime_wealth_dict_result-->",type(disable_classtime_wealth_dict_result))

                    #未开启财富dict类型合并为另外一个dict类型
                    disable_wealth_dict_result = dict(list(disable_point_wealth_dict_result.items()) +
                                                      list(disable_classtime_wealth_dict_result.items()))

                elif (str(user_role_info) == "12"):

                    #获取用户未开启北美课时
                    disable_na_pri_wealth_dict_result = talk_query_user_assets_disable_na_pri_user_wealth_success(user_id)

                    #获取用户未开启北美绘本课
                    disable_na_open_wealth_dict_result = talk_query_user_assets_disable_na_open_user_wealth_success(user_id)

                    #未开启财富dict类型合并为另外一个dict类型
                    disable_wealth_dict_result = dict(list(disable_na_pri_wealth_dict_result.items()) +
                                                      list(disable_na_open_wealth_dict_result.items()))

                disable_wealth_list_result.append(disable_wealth_dict_result)
                # print ("disable_wealth_list_result-->",disable_wealth_list_result)
                # print ("disable_wealth_list_result-->",type(disable_wealth_list_result))

                # cursor_point.close()
                # conn_point.close()

                user_detail_dict = {

                    "user_list":user_list_result,
                    "enable_wealth_list":enable_wealth_list_result,
                    "disable_wealth_list":disable_wealth_list_result,
                    "userRole":user_role_info
                }

                print ("user_detail_dict-->",user_detail_dict)
                print ("type(user_detail_dict)-->",type(user_detail_dict))

                #注释：or wealth_list_result == ()


                return JsonResponse({"status_code":10200,
                                     "message":"用户信息获取成功！！！",
                                     "result":user_detail_dict})


'''###############################################################################'''
#获取用户未处理的订单信息
@auth
def get_order_on_detail(request):

    if request.method == "POST":

        user_mobile = request.POST.get("userMobile","")

        if user_mobile == "":

            return JsonResponse({"status_code":10101,"message":"用户手机号不能为空！"})

        elif len(user_mobile) < 11 or len(user_mobile) > 11:

            return JsonResponse({"status_code":10102,
                                 "message":"用户手机号输入错误，请重新输入！"})

        else:

            userId = talk_query_user_info_id_success(user_mobile)

            status = 'on'

            order_list_result = talk_query_user_order2_success(userId,status)

            if order_list_result == ():

                return JsonResponse({"status_code":10103,"message":"该用户还未下单！！！"})

            else:

                return JsonResponse({"status_code":10200,"message":"用户未完成订单获取成功！！！","result":order_list_result})
