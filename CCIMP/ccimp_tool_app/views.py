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
from externalClass.smsLoginSmsCode import smsLoginCode
from externalClass.smsLoginSmsContent import smsLoginSmsContent
from externalClass.mobileNumberFormatValidity import mobileNumberFormatValidity
from externalClass.nickName import nickName
from externalClass.accountStatus import accountStatus
from externalClass.mobileStatus import mobileStatus
from externalClass.userIdentity import userIdentity
from externalClass.getSessionUser import getSessionUser
from externalClass.courseStatus import courseStatus
from externalClass.open_class.getTeacherInfo import getTeacherInfo
from externalClass.open_class.getTextBookInfo import getTextBookInfo
from externalClass.open_class.getOpenClassInfo import getOpenClassInfo
from externalClass.open_class.openClassConfig import *
from externalClass.getRegisterInfo import is_used_phoneNumber
from externalClass.postRegisterinfo import post_registerinfo
from externalClass.postrUserOccupInfo import UpUserOccupInfo
from externalClass.appoint.getTalkAppointInfo import getTalkAppointInfo
from externalClass.appoint.getTalkPlatformAppointReconstructionAppointInfo import getTalkPlatformAppointReconstructionAppointInfo
from externalClass.appoint.appointConfig import *
from externalClass.ssoIdentity import ssoIdentity

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
from db_config.talkQueryUserInfo import talk_query_user_info_id_account_status_success

from db_config.talkQueryAppointInfo import talk_query_appoint_info_detail_success
from db_config.talkQueryAppointInfo import talk_query_appoint_info_id_success

from db_config.talkQueryAppointInfo import talk_update_appoint_info_start_time_end_time_success
from db_config.talkQueryAppointInfo import talkplatform_appoint_reconstruction_update_appoint_info_start_time_end_time_success


from db_config.db_config import *

import json
import time
import requests

from datetime import datetime,timedelta

from db_config.talkQueryUserOrder import talk_platform_order_query_user_order_success
from db_config.talkQueryUserOrder import talk_platform_order_query_user_order2_success


'''###############################################################################'''
from externalClass.ssoH5 import ssoH5_modify,ssoH5_query


'''###############################################################################'''
#定义全局变量
requestSession = ''


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
                                   "type_option_admin":"permission_sap",
                                   "aTag_":"2"})

                elif user.permission_options == 2:

                    return render(request,"tool_sale_order.html",
                                  {"username":get_username,
                                   "aTag_":"2"})

                elif user.permission_options == 3:

                    return render(request,"tool_sale_order.html",
                                  {"username":get_username,
                                   "aTag_":"2"})


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

        elif len(user_password)< 6 or len(user_password)>20:

            # return HttpResponse("用户密码输入错误，请重新输入！")
            return JsonResponse({"status_code":10106,
                                 "message":"用户密码输入错误，请重新输入！"})
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

                print (user_id)

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
                                         "message":"获取所有套餐数据为空，请查看原因！！！",
                                         "result":point_info,
                                         "user_role":user_role_info})
                else:

                    return JsonResponse({"status_code":10200,
                                         "message":"获取套餐数据成功！！！",
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
                # print ("status_flage-->",status_flage)

                if status_flage == False:

                    return JsonResponse({"status_code":10105,
                                         "message":"签名获取失败，不能创建订单数据！"})

                elif status_flage == '订单id获取失败！':

                    return JsonResponse({"status_code":10106,
                                         "message":"订单创建失败，请查看原因！",
                                         "result":status_flage})

                else:

                    return JsonResponse({"status_code":10200,
                                         "message":"下单成功",
                                         "result":status_flage})


'''###############################################################################'''
#获取订单详情
@auth
def get_order_detail(request):

    if request.method == "POST":

        order_id = request.POST.get("order_id","")

        #获取订单详情
        order_detail = talk_platform_order_query_user_order_success(order_id)

        # cursor_talk.close()
        # conn_talk.close()

        if order_detail == ():

            return JsonResponse({"status_code":10101,
                                 "message":"订单获取失败，无法读取新创建的订单数据！！！"})

        else:

            return JsonResponse({"status_code":10200,
                                 "message":"订单获取成功！！！",
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
                                     "message":"订单处理成功！！！"})

            else:

                return JsonResponse({"status_code":10102,
                                     "message":"订单处理失败！！！"})


'''###############################################################################'''
#获取用户未处理的订单信息
@auth
def get_order_on_detail(request):

    if request.method == "POST":

        user_mobile = request.POST.get("userMobile","")
        user_password = request.POST.get("userPasword","")

        if user_mobile == "":

            return JsonResponse({"status_code":10101,"message":"用户手机号不能为空！"})

        elif user_password == "":

            # return HttpResponse("用户密码不能为空！")
            return JsonResponse({"status_code":10104,"message":"用户密码不能为空！"})

        elif len(user_mobile) < 11 or len(user_mobile) > 11:

            return JsonResponse({"status_code":10102,"message":"用户手机号输入错误，请重新输入！"})

        elif len(user_password)< 6 or len(user_password)>20:

            # return HttpResponse("用户手机号输入错误，请重新输入！")
            return JsonResponse({"status_code":10105,
                                 "message":"用户密码输入错误，请重新输入！"})

        else:

            #调用获取加密密码接口
            pwd = publicKeyRsa(user_password)

            #调用获取登录状态接口
            req = userLogin(user_mobile,pwd)

            #登录错误或者不是内部网络
            if req == global_configure.login_error_message:

                return JsonResponse({"status_code":10100,"message":req})
            #     return HttpResponse("用户密码不能为空！")

            else:

                userId = talk_query_user_info_id_success(user_mobile)

                limit_sum = 10

                order_list_result = talk_platform_order_query_user_order2_success(userId,limit_sum)

                if order_list_result == ():

                    return JsonResponse({"status_code":10103,"message":"该用户还未下单！！！"})

                else:

                    return JsonResponse({"status_code":10200,"message":"用户未完成订单获取成功！！！","result":order_list_result})


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
                                   "type_option_admin":"permission_sap",
                                   "aTag_":"2"})

                elif user.permission_options == 2:

                    return render(request,"tool_user_info.html",
                                  {"username":get_username,
                                   "aTag_":"2"})

                elif user.permission_options == 3:

                    return render(request,"tool_user_info.html",
                                  {"username":get_username,
                                   "aTag_":"2"})


'''###############################################################################'''
#获取用户信息详情
@auth
def get_userinfo_detail(request):

    if request.method == "POST":

        user_detail_dict = {}

        disable_wealth_list_result = []

        disable_wealth_dict_result = {}

        user_mobile = request.POST.get("userMobile","")

        #1:用户手机号不能为空！;2:手机号位数输入错误，请重新输入！;3:手机号格式输入错误，请重新输入！;4:正常
        mobile_result_tag = mobileNumberFormatValidity(user_mobile)
        # print ("mobile_result_tag",mobile_result_tag)

        if mobile_result_tag == 1:

            # return HttpResponse("用户手机号不能为空！")
            return JsonResponse({"status_code":10101,
                                 "message":"手机号不能为空！"})

        elif mobile_result_tag == 2:

            # return HttpResponse("手机号位数输入错误，请重新输入！")
            return JsonResponse({"status_code":10102,
                                 "message":"手机号位数输入错误，请重新输入！"})

        elif mobile_result_tag == 3:

            # return HttpResponse("手机号格式输入错误，请重新输入！")
            return JsonResponse({"status_code":10106,
                                 "message":"手机号格式输入错误，请重新输入！"})

        elif mobile_result_tag == 4:

            #获取用户信息详情
            user_list_result = talk_query_user_info_detail_success(user_mobile)
            # print ("user_list_result-->",user_list_result)
            # print ("user_list_result-->",type(user_list_result))

            # cursor_talk.close()
            # conn_talk.close()

            if user_list_result == ():

                return JsonResponse({"status_code":10103,
                                     "message":"无法获取该用户信息或该用户为冻结状态！！！"})

            else:

                user_id = talk_query_user_info_id_success(user_mobile)
                # print ("user_id-->",user_id)

                # print ("user_id-->",type(user_id))

                #获取用户身份
                user_role_info = getUserRole(user_id)
                # print (user_role_info)
                # print (type(user_role_info))

                # 获取用户身份失败或当前网络不是测试环境
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

                # print ("user_detail_dict-->",user_detail_dict)
                # print ("type(user_detail_dict)-->",type(user_detail_dict))

                #注释：or wealth_list_result == ()


                return JsonResponse({"status_code":10200,
                                     "message":"用户信息获取成功！！！",
                                     "result":user_detail_dict})


'''###############################################################################'''
#获取学员手机短信内容
@auth
def get_user_sms_connent(request):

    if request.method == "POST":

        user_mobile = request.POST.get("userMobile","")

        #获取短信搜索内容
        search_content = request.POST.get("searchContent", "")
        # print ("search_content",search_content)

        #1:用户手机号不能为空！;2:手机号位数输入错误，请重新输入！;3:手机号格式输入错误，请重新输入！;4:正常
        mobile_result_tag = mobileNumberFormatValidity(user_mobile)
        # print ("mobile_result_tag",mobile_result_tag)

        if mobile_result_tag == 1:

            # return HttpResponse("用户手机号不能为空！")
            return JsonResponse({"status_code":10100,
                                 "message":"手机号不能为空！"})

        elif mobile_result_tag == 2:

            # return HttpResponse("手机号位数输入错误，请重新输入！")
            return JsonResponse({"status_code":10101,
                                 "message":"手机号位数输入错误，请重新输入！"})

        elif mobile_result_tag == 3:

            # return HttpResponse("手机号格式输入错误，请重新输入！")
            return JsonResponse({"status_code":10102,
                                 "message":"手机号格式输入错误，请重新输入！"})

        elif mobile_result_tag == 4:

            sms_code = smsLoginCode('zhangbo','zhangbo2019',user_mobile)

            #添加了搜索内容字段
            sms_content = smsLoginSmsContent('zhangbo','zhangbo2019',user_mobile,search_content)

            if sms_code == None and sms_content == None:

                return JsonResponse({"status_code":10103,
                                     "message":"未找到该手机的短信信息！！！"})

            elif sms_code != None and sms_content != None:

                return JsonResponse({"status_code":10200,
                                     "message":"手机的短信信息获取成功！！！",
                                     "result_sms_code":sms_code,
                                     "result_sms_content":sms_content})

            elif sms_code != None and sms_content == None:

                return JsonResponse({"status_code":10200,
                                     "message":"手机验证码获取成功！！！",
                                     "result_sms_code":sms_code,
                                     "result_sms_content":""})

            elif sms_code == None and sms_content != None:

                return JsonResponse({"status_code":10200,
                                     "message":"该手机短信内容获取成功！！！",
                                     "result_sms_code":"",
                                     "result_sms_content":sms_content})


'''###############################################################################'''
# 给用户添加次卡
@auth
def add_user_point(request):

    message = ""

    get_username = getSessionUser(request)

    users = User.objects.all()

    if request.method == "POST":
        userid = request.POST.get("userid")
        points = request.POST.get("point")

        interfeceurl = "http://172.16.16.97/talkplatform_point_consumer/v2/user_asset/add_gift_asset_last_order"
        postdata = {
            'sn': 'web',
            'sku_type_name': 'point',
            'count': '%s' % points,
            'days': '%s' % points,
            'transaction_type_code': 'add_gift_asset',
            'stu_id': '%s' % userid,
            'remark': '测试添加次卡数',
            'operator_id': '0',
            'timestamp': '1111',
            'sub_gift_code': 'add_gift_asset_crm_web_award',
            'appkey': '11'
        }

        try:
            req = adminLogin()
            addrequest = req.post(interfeceurl, postdata)
            message = addrequest.text
        except BaseException as msg:
            message = msg
        if "success" in message:
            message = "次卡添加成功"
        elif message == '1':
            message = "体验课次卡添加成功"

    for user in users:

        if user.user_name == get_username:

            if user.permission_options == 1:

                return render(request, "tool_adduserpoint.html", {"message": message,"username": get_username,
                                                                  "type_option_admin": "permission_sap",
                                                                  "aTag_":"2"})

            else:

                return render(request, "tool_adduserpoint.html", {"message": message,"username": get_username,
                                                                  "aTag_":"2"})


'''###############################################################################'''
#用户昵称修改
@auth
def user_nick_name(request):

    if request.method == "POST":

        user_nickName = request.POST.get("nickName","")

        user_mobile = request.POST.get("userMobile","")

        # print (user_nickName)
        # print (user_mobile)

        #1:用户手机号不能为空！;2:手机号位数输入错误，请重新输入！;3:手机号格式输入错误，请重新输入！;4:正常
        mobile_result_tag = mobileNumberFormatValidity(user_mobile)
        # print ("mobile_result_tag",mobile_result_tag)

        if mobile_result_tag == 1:

            # return HttpResponse("用户手机号不能为空！")
            return JsonResponse({"status_code":10101,
                                 "message":"手机号不能为空！"})

        elif mobile_result_tag == 2:

            # return HttpResponse("手机号位数输入错误，请重新输入！")
            return JsonResponse({"status_code":10102,
                                 "message":"手机号位数输入错误，请重新输入！"})

        elif mobile_result_tag == 3:

            # return HttpResponse("手机号格式输入错误，请重新输入！")
            return JsonResponse({"status_code":10103,
                                 "message":"手机号格式输入错误，请重新输入！"})

        elif mobile_result_tag == 4:

            if user_nickName == "":

                return JsonResponse({"status_code":10104,
                                     "message":"用户昵称为空"})

            l_user_nick_name = len(user_nickName)

            if l_user_nick_name > 16:

                return JsonResponse({"status_code":10105,
                                     "message":"用户昵称过长，你重新输入"})

            userId = talk_query_user_info_id_success(user_mobile)

            nickname_result = nickName(user_nickName,userId)
            # print (type(nickname_result))

            if nickname_result == '1':

                return JsonResponse({"status_code": 10200,"message":"用户昵称修改成功"})

            elif nickname_result == '修改失败':

                return JsonResponse({"status_code": 10106,
                                     "message": "昵称数据异常，昵称不能是中文字符"})

            elif nickname_result == '学员已冻结，不能修改信息':

                return JsonResponse({"status_code": 10107,
                                     "message": "学员已冻结，不能修改信息"})


'''###############################################################################'''
#新账号注册检测
@auth
def register_mobile_check(request):

    if request.method == "POST":

        user_mobile = request.POST.get("new_mobile", "")

        get_mobile_status = is_used_phoneNumber(user_mobile)

        if get_mobile_status == '1' :

            return JsonResponse({"status_code": 10200,"message":"手机号未注册"})

        elif get_mobile_status == '0':

            return JsonResponse({"status_code": 10101,"message":"手机号已注册"})

        else :

            return JsonResponse({"status_code": 10102,"message":"其他错误"})

        #print(get_mobile_status)


'''###############################################################################'''
#账号注册
@auth
def post_registerinfo_mobile(request):

    if request.method == "POST":

        new_mobile = request.POST.get("new_mobile", "")

        new_password = request.POST.get("new_password", "")

        recommen_mobile = request.POST.get("recommen_mobile", "")

        get_register_status = post_registerinfo(new_mobile,new_password,recommen_mobile)
        print (get_register_status)

        if get_register_status["statue"] == 'OK':

            global requestSession

            requestSession = get_register_status["requestSession"]

            return JsonResponse({"status_code": 10200,"message":"注册成功"})

        elif get_register_status[0] == '0':

            return JsonResponse({"status_code": 10101,"message":"手机号已注册"})

        else:

            return JsonResponse({"status_code": 10201,"message":"注册失败"})


'''###############################################################################'''
#账号注册后修改用户身份选项
def post_UpUserOccupInfo(request):

    if request.method == "POST":

       levelRoleData = request.POST

       res = UpUserOccupInfo(levelRoleData,requestSession)

       return JsonResponse({"status_code": 10200, "message": "身份选项设置成功！"})


'''###############################################################################'''
#账号状态修改
@auth
def account_status(request):

    if request.method == "GET":

        user_mobile = request.GET.get("userMobile","")
        account_status = request.GET.get("accountStatus","")

        # print ("user_mobile-->",user_mobile)
        # print ("account_status-->",account_status)

        #1:用户手机号不能为空！;2:手机号位数输入错误，请重新输入！;3:手机号格式输入错误，请重新输入！;4:正常
        mobile_result_tag = mobileNumberFormatValidity(user_mobile)
        # print ("mobile_result_tag",mobile_result_tag)

        if mobile_result_tag == 1:

            # return HttpResponse("用户手机号不能为空！")
            return JsonResponse({"status_code":10101,
                                 "message":"手机号不能为空！"})

        elif mobile_result_tag == 2:

            # return HttpResponse("手机号位数输入错误，请重新输入！")
            return JsonResponse({"status_code":10102,
                                 "message":"手机号位数输入错误，请重新输入！"})

        elif mobile_result_tag == 3:

            # return HttpResponse("手机号格式输入错误，请重新输入！")
            return JsonResponse({"status_code":10103,
                                 "message":"手机号格式输入错误，请重新输入！"})

        elif mobile_result_tag == 4:

            if account_status == "freeze":

                account_status = account_status

            elif account_status == "on":

                account_status = account_status

            #查询账号状态返回用户id
            userId = talk_query_user_info_id_account_status_success(user_mobile)

            accountstatus_result = accountStatus(account_status,userId)

            if accountstatus_result == True:

                return JsonResponse({"status_code": 10200,"message":"账号状态修改成功"})

            elif accountstatus_result == False:

                return JsonResponse({"status_code": 10104,
                                     "message": "账号状态修改失败"})


'''###############################################################################'''
#手机号状态修改
@auth
def mobile_status(request):

    if request.method == "POST":

        is_check = request.POST.get("isCheck","")

        user_mobile = request.POST.get("userMobile","")

        # print (is_check)
        # print (user_mobile)

        #1:用户手机号不能为空！;2:手机号位数输入错误，请重新输入！;3:手机号格式输入错误，请重新输入！;4:正常
        mobile_result_tag = mobileNumberFormatValidity(user_mobile)
        # print ("mobile_result_tag",mobile_result_tag)

        if mobile_result_tag == 1:

            # return HttpResponse("用户手机号不能为空！")
            return JsonResponse({"status_code":10101,
                                 "message":"手机号不能为空！"})

        elif mobile_result_tag == 2:

            # return HttpResponse("手机号位数输入错误，请重新输入！")
            return JsonResponse({"status_code":10102,
                                 "message":"手机号位数输入错误，请重新输入！"})

        elif mobile_result_tag == 3:

            # return HttpResponse("手机号格式输入错误，请重新输入！")
            return JsonResponse({"status_code":10103,
                                 "message":"手机号格式输入错误，请重新输入！"})

        elif mobile_result_tag == 4:

            if is_check == "y":

                is_check = is_check

            elif is_check == "n":

                is_check = is_check


            userId = talk_query_user_info_id_success(user_mobile)

            if userId == ():

                return JsonResponse({"status_code": 10104,"message":"该学员对应的userid为空"})


            mobilestatus_result = mobileStatus(is_check,userId)
            # print (type(mobilestatus_result))

            if mobilestatus_result == '1':

                return JsonResponse({"status_code": 10200,"message":"手机号状态已修改"})

            elif mobilestatus_result == '修改失败':

                return JsonResponse({"status_code": 10105,
                                     "message": "手机号状态修改失败"})


'''###############################################################################'''
#用户身份状态修改
@auth
def user_identity(request):

    if request.method == "POST":

        is_buy = request.POST.get("isBuy","")

        user_mobile = request.POST.get("userMobile","")

        # print (is_buy)
        # print (user_mobile)

        #1:用户手机号不能为空！;2:手机号位数输入错误，请重新输入！;3:手机号格式输入错误，请重新输入！;4:正常
        mobile_result_tag = mobileNumberFormatValidity(user_mobile)
        # print ("mobile_result_tag",mobile_result_tag)

        if mobile_result_tag == 1:

            # return HttpResponse("用户手机号不能为空！")
            return JsonResponse({"status_code":10101,
                                 "message":"手机号不能为空！"})

        elif mobile_result_tag == 2:

            # return HttpResponse("手机号位数输入错误，请重新输入！")
            return JsonResponse({"status_code":10102,
                                 "message":"手机号位数输入错误，请重新输入！"})

        elif mobile_result_tag == 3:

            # return HttpResponse("手机号格式输入错误，请重新输入！")
            return JsonResponse({"status_code":10103,
                                 "message":"手机号格式输入错误，请重新输入！"})

        elif mobile_result_tag == 4:

            if is_buy == "free":

                is_buy = is_buy

            elif is_buy == "buy":

                is_buy = is_buy


            userId = talk_query_user_info_id_success(user_mobile)

            if userId == ():

                return JsonResponse({"status_code": 10104,"message":"该学员对应的userid为空"})

            useridentity_result = userIdentity(is_buy,userId)
            # print (type(useridentity_result))

            if useridentity_result == '1':

                return JsonResponse({"status_code": 10200,"message":"用户身份已修改"})

            elif useridentity_result == '修改失败':

                return JsonResponse({"status_code": 10105,
                                     "message": "用户身份修改失败"})


'''###############################################################################'''
# 2020-07-05:张波修改
#课程状态修改
# @auth
# def course_status(request):

    # if request.method == "GET":
    #
    #     course_status = request.GET.get("courseStatus","")
    #     user_mobile = request.GET.get("userMobile","")
    #
    #     # print (course_status)
    #     # print (user_mobile)
    #
    #     # 1:用户手机号不能为空！;2:手机号位数输入错误，请重新输入！;3:手机号格式输入错误，请重新输入！;4:正常
    #     mobile_result_tag = mobileNumberFormatValidity(user_mobile)
    #     # print ("mobile_result_tag",mobile_result_tag)
    #
    #     if mobile_result_tag == 1:
    #
    #         # return HttpResponse("用户手机号不能为空！")
    #         return JsonResponse({"status_code": 10101,
    #                              "message": "手机号不能为空！"})
    #
    #     elif mobile_result_tag == 2:
    #
    #         # return HttpResponse("手机号位数输入错误，请重新输入！")
    #         return JsonResponse({"status_code": 10102,
    #                              "message": "手机号位数输入错误，请重新输入！"})
    #
    #     elif mobile_result_tag == 3:
    #
    #         # return HttpResponse("手机号格式输入错误，请重新输入！")
    #         return JsonResponse({"status_code": 10103,
    #                              "message": "手机号格式输入错误，请重新输入！"})
    #
    #     elif mobile_result_tag == 4:
    #
    #         if course_status == "end":
    #
    #             course_status = course_status
    #
    #         elif course_status == "s_absent":
    #
    #             course_status = course_status
    #
    #         elif course_status == "t_absent":
    #
    #             course_status = course_status
    #
    #         userId = talk_query_user_info_id_success(user_mobile)
    #         # print ("用户id：",userId)
    #         # print (type(userId))
    #
    #         if userId == ():
    #
    #             return JsonResponse({"status_code": 10104,"message":"该学员对应的userid为空"})
    #
    #         #约课数据
    #         # appoint_id_data = talk_query_appoint_info_detail_success(userId)
    #         appoint_id_data = talk_query_appoint_info_id_success(userId)
    #         # print ("约课数据：",appoint_id_data)
    #         # print ("约课数据类型：",type(appoint_id_data))
    #
    #         if appoint_id_data == ():
    #
    #             return JsonResponse({"status_code": 10105,"message":"该学员对应的appointid为空"})
    #
    #         course_status_result = courseStatus(course_status,appoint_id_data)
    #         # print (type(course_status_result))
    #
    #         if course_status_result == True:
    #
    #             return JsonResponse({"status_code": 10200,"message":"课程状态已修改"})
    #
    #         elif course_status_result == False:
    #
    #             return JsonResponse({"status_code": 10106,
    #                                  "message": "课程状态修改失败"})


'''###############################################################################'''
#公开课manage
@auth
def open_class(request):

    get_username = getSessionUser(request)

    users = User.objects.all()

    open_class_info_result_list = getOpenClassInfo(course_limit_sum)


    if request.method == "GET":

        for user in users:

            if user.user_name == get_username:

                if user.permission_options == 1:

                    return render(request,"open_class.html",
                                  {"username":get_username,
                                   "type_option_admin":"permission_sap",
                                   "aTag_":"2",
                                   "type":"list",
                                   "openClasss":open_class_info_result_list})

                elif user.permission_options == 2:

                    return render(request,"open_class.html",
                                  {"username":get_username,
                                   "aTag_":"2",
                                   "type":"list",
                                   "openClasss": open_class_info_result_list})

                elif user.permission_options == 3:

                    return render(request,"open_class.html",
                                  {"username":get_username,
                                   "aTag_":"2",
                                   "type":"list",
                                   "openClasss": open_class_info_result_list})


'''###############################################################################'''
#公开课添加
@auth
def open_class_add(request):

    '''公开课开课'''

    get_username = request.session.get('user', '')

    if request.method == "GET":

        user = User.objects.get(user_name=get_username)

        if user.user_name == get_username:

            if user.permission_options == 1:

                    return render(request,"open_class_add.html",
                                  {"username":get_username,
                                   "type":"add",
                                   "type_option_admin":"permission_sap",
                                   "aTag_":"2"})

            elif user.permission_options == 2:

                    return render(request,"open_class_add.html",
                                  {"username":get_username,
                                   "type":"add",
                                   "aTag_":"2"})

            elif user.permission_options == 3:

                    return render(request, "open_class_add.html",
                                  {"username": get_username,
                                   "aTag_": "2",
                                   "type": "add"})

        else:

            pass

    else:

        open_class_name = request.POST.get("openClassName", "")
        capacity_name = request.POST.get("capacityName", "")
        teacher_name = request.POST.get("teacherName", "")
        cost_type_name = request.POST.get("costTypeName", "")
        code_item_id_name = request.POST.get("codeItemIdName", "")
        code_num_name = request.POST.get("codeNumName", "")
        priority_name = request.POST.get("priorityName", "")
        course_type_name = request.POST.get("courseTypeName", "")
        book_type_name = request.POST.get("bookTypeName", "")
        book_text_name_1 = request.POST.get("bookText1Name", "")
        book_text_name_2 = request.POST.get("bookText2Name", "")
        book_text_name_3 = request.POST.get("bookText3Name", "")
        open_class_start_time = request.POST.get("openClassStartTime", "")
        open_class_end_time = request.POST.get("openClassEndTime", "")

        open_class_start_time = open_class_start_time + ":00"
        open_class_end_time   = open_class_end_time + ":00"
        # print (open_class_start_time)
        # print (open_class_end_time)

        start_time_compare = datetime.strptime(open_class_start_time, "%Y-%m-%d %H:%M:%S")
        end_time_compare = datetime.strptime(open_class_end_time, "%Y-%m-%d %H:%M:%S")

        time_seconds_int = int((end_time_compare - start_time_compare).total_seconds())

        if (time_seconds_int <= 600 ):

            return JsonResponse({"status": 10002, "message": "开课时间不能小于10分钟"})

        addAppointOpenClassUrl = "http://172.16.16.97/talkplatform_course_consumer/course_open_class/add_course_info"

        c_course_costs = [{"cost_type":cost_type_name,"code_item_id":code_item_id_name,"code_num":code_num_name,"priority":priority_name}]

        c_course_costs = json.dumps(c_course_costs)


        #公开课能预约开始时间(str)
        appoint_start_time = datetime.utcfromtimestamp(time.time() + 29000)
        # print ("appoint_start_time-->",appoint_start_time,type(appoint_start_time))
        appoint_start_time = appoint_start_time.strftime('%Y-%m-%d %H:%M:%S')
        # print ("appoint_start_time-->",appoint_start_time,type(appoint_start_time))


        # 公开课能预约结束时间(str)
        appoint_end_time = datetime.now().date() + timedelta(days=7)
        # print ("appoint_end_time-->",appoint_end_time,type(appoint_end_time))
        appoint_end_time = appoint_end_time.strftime('%Y-%m-%d %H:%M:%S')
        # print ("appoint_end_time-->",appoint_end_time,type(appoint_end_time))


        open_class_start_time_1 = datetime.strptime(open_class_start_time, "%Y-%m-%d %H:%M:%S")
        appoint_end_time_1 = datetime.strptime(appoint_end_time, "%Y-%m-%d %H:%M:%S")

        time_seconds_int = int((open_class_start_time_1 - appoint_end_time_1).total_seconds())

        if (time_seconds_int >= 0):

            return JsonResponse({"status": 10003, "message": "公开课开课时间不能大于7天"})

        #接口调用传值
        addAppointOpenClassData = {
            "name": open_class_name,
            "name_en": "csopenclass",
            "name_zh": open_class_name,
            "intro": "测试公共课勿动",
            "intro_desc": "zb",
            "description": "测试公开课",
            "content": "zb",
            "cover": "zb.jpg",
            "sort": "10",
            "book_type": book_type_name,
            "book_id": book_text_name_3,
            "capacity": capacity_name,
            "course_type": course_type_name,
            "c_cate_id1": book_text_name_1,
            "c_cate_id2": book_text_name_2,
            "c_enlevel_id": "1",
            "c_occup_id": "1",
            "c_tea_ids": teacher_name,
            "c_course_costs": c_course_costs,
            "appoint_start_time": appoint_start_time,
            "appoint_end_time": appoint_end_time,
            "start_time": open_class_start_time,
            "end_time": open_class_end_time,
            "is_recommend": "1",
            "study_type": "0",
            "get_skill": "技能测试",
            "class_state": "1",
            "status": "1",
            "admin_id": "1",
            "occup_people": "0",
            "stu_type": "junior",
            "tea_type": "1",
            "sdk_type": "8",
            "tag": "公开课 测试课",
            "channel[]": "51talk-web"
        }

        # 转换为datetime.datetime类型
        current_now_time = datetime.now()

        # 转换为str类型
        current_now_time_y_m_d = current_now_time.strftime('%Y-%m-%d %H:%M:%S')

        #由字符串格式转化为日期格式的函数为: datetime.datetime.strptime()
        appoint_start_time = datetime.strptime(appoint_start_time, "%Y-%m-%d %H:%M:%S")
        print (appoint_start_time,type(appoint_start_time))

        current_now_time_y_m_d = datetime.strptime(current_now_time_y_m_d, "%Y-%m-%d %H:%M:%S")
        print (current_now_time_y_m_d,type(current_now_time_y_m_d))

        seconds_int = int((appoint_start_time - current_now_time_y_m_d).total_seconds())
        print (seconds_int)

        if (seconds_int >= 0):

            open_class_result_json = requests.post(url=addAppointOpenClassUrl, data=addAppointOpenClassData)
            # print(open_class_result_json.json())

            open_class_result_code = int(open_class_result_json.json()['code'])
            # print(open_class_result_code)
            # print(type(open_class_result_code))

            open_class_result_message = open_class_result_json.json()['message']


            if open_class_result_code == 10000:

                return JsonResponse({"status": 200, "message": "公开课开课成功！"})

            else:

                return JsonResponse({"status": 10000, "message": open_class_result_message})

        else:

            open_class_result_json = requests.post(url=addAppointOpenClassUrl, data=addAppointOpenClassData)
            # print(open_class_result_json.json())

            open_class_result_code = int(open_class_result_json.json()['code'])
            # print(open_class_result_code)
            # print(type(open_class_result_code))

            open_class_result_message = open_class_result_json.json()['message']

            if open_class_result_code == 10030:

                return JsonResponse({"status": 10001, "message": open_class_result_message})


'''###############################################################################'''
#获得老师list数据
@auth
def getSelectTeacherData(request):

    if request.method == "GET":

        teacherinfo_result_list = getTeacherInfo(limin_teacher_sum)

        teacherinfo_result_no = {}

        if teacherinfo_result_list == ():

            teacherinfo_result_no = {

                "info": "老师查询无结果",
            }

            return JsonResponse({"status": 10100, "message": "success", "data": teacherinfo_result_no})

        else:

            return JsonResponse({"status": 10200, "message": "success", "data": teacherinfo_result_list})


'''###############################################################################'''
#获得教材list数据
@auth
def getSelectTextBookData(request):

    if request.method == "GET":

        textbookinfo_result_list = getTextBookInfo(c_cate1_textbook_limit_sum,c_cate2_textbook_limit_sum,c_cate3_textbook_limit_sum)

        textbookinfo_result_no = {}

        if textbookinfo_result_list == ():

            textbookinfo_result_no = {

                "info": "教材查询无结果",
            }

            return JsonResponse({"status": 10100, "message": "success", "data": textbookinfo_result_no})

        else:

            return JsonResponse({"status": 10200, "message": "success", "data": textbookinfo_result_list})


'''###############################################################################'''
#2020-07-05:张波修改
#获取约课记录数据
@auth
def get_user_appoint_record(request):

    if request.method == "GET":

        user_mobile = request.GET.get("userMobile","")

        # 1:用户手机号不能为空！;2:手机号位数输入错误，请重新输入！;3:手机号格式输入错误，请重新输入！;4:正常
        mobile_result_tag = mobileNumberFormatValidity(user_mobile)
        # print ("mobile_result_tag",mobile_result_tag)

        if mobile_result_tag == 1:

            # return HttpResponse("用户手机号不能为空！")
            return JsonResponse({"status_code": 10101,
                                 "message": "手机号不能为空！"})

        elif mobile_result_tag == 2:

            # return HttpResponse("手机号位数输入错误，请重新输入！")
            return JsonResponse({"status_code": 10102,
                                 "message": "手机号位数输入错误，请重新输入！"})

        elif mobile_result_tag == 3:

            # return HttpResponse("手机号格式输入错误，请重新输入！")
            return JsonResponse({"status_code": 10103,
                                 "message": "手机号格式输入错误，请重新输入！"})

        userId = talk_query_user_info_id_success(user_mobile)

        if userId == ():

            return JsonResponse({"status_code": 10104,"message":"该学员对应的userid为空"})

        #获取talk约课记录
        talk_appoint_info_result = getTalkAppointInfo(userId,limit_appoint_sum)
        # print (talk_appoint_info_result)

        #获取talkplatform_appoint_reconstruction约课记录
        talkplatform_appoint_reconstruction_appoint_info_result = getTalkPlatformAppointReconstructionAppointInfo(userId,limit_appoint_sum)
        # print (talkplatform_appoint_reconstruction_appoint_info_result)

        if talk_appoint_info_result == [] and talkplatform_appoint_reconstruction_appoint_info_result == []:

            return JsonResponse({"status_code": 10105,"message":"该学员约课信息在php库与平台库查询为空"})

        elif talk_appoint_info_result == []:

            return JsonResponse({"status_code": 10106, "message": "该学员约课信息在php库查询为空"})

        elif talkplatform_appoint_reconstruction_appoint_info_result == []:

            return JsonResponse({"status_code": 10107, "message": "该学员约课信息在平台库查询为空"})

        # return JsonResponse({"status_code": 10200,
        #                      "result": {"data":"接口获取正确"}})

        return JsonResponse({"status_code": 10200, "data": "接口获取正确",
                             "appointRecords":talkplatform_appoint_reconstruction_appoint_info_result})


'''###############################################################################'''
#2020-07-11:张波修改--获取数据方法二合一，暂时屏蔽这个方法
#初始化获得约课记录list数据
# @auth
# def getAppointRecordListData(request):
#
#     if request.method == "GET":
#
#         user_mobile = request.GET.get("userMobile","")
#         # print ("user_mobile-->",user_mobile)
#
#         userId = talk_query_user_info_id_success(user_mobile)
#
#         talkplatform_appoint_reconstruction_appoint_info_result = getTalkPlatformAppointReconstructionAppointInfo(userId,limit_appoint_sum)
#         # print (talkplatform_appoint_reconstruction_appoint_info_result)
#
#         return JsonResponse({"status_code": 10200, "data": "接口获取正确",
#                              "appointRecords":talkplatform_appoint_reconstruction_appoint_info_result})


'''###############################################################################'''
#2020-07-05:张波修改
#修改课程状态数据
@auth
def appoint_record(request):

    if request.method == "POST":

        appoint_record_id = request.POST.get("appointRecordID","")
        course_status = request.POST.get("courseStatus","")

        if course_status == "end":

            course_status = course_status

        elif course_status == "s_absent":

            course_status = course_status

        elif course_status == "t_absent":

            course_status = course_status

        try:

            # 转换为datetime.datetime类型
            current_now_time = datetime.utcfromtimestamp(time.time() + 28800)
            print(current_now_time)

            # 转换为str类型
            current_now_time = current_now_time.strftime('%Y-%m-%d %H:%M:%S')
            print(current_now_time)

            course_status_result = courseStatus(course_status,appoint_record_id)
            print (course_status_result)

            if course_status_result == True:

                talk_update_appoint_info_start_time_end_time_success(appoint_record_id,
                                                                     current_now_time,
                                                                     current_now_time)

                talkplatform_appoint_reconstruction_update_appoint_info_start_time_end_time_success(appoint_record_id,
                                                                                                    current_now_time,
                                                                                                    current_now_time)

                return JsonResponse({"status_code": 10200,"message":"课程状态已修改"})

            elif course_status_result == False:

                return JsonResponse({"status_code": 10101,"message": "课程状态修改失败"})

        except:

            return JsonResponse({"status_code": 10102,"message":"课程更新出错"})


'''###############################################################################'''
#2020-07-25:张波修改
#sso身份修改
@auth
def sso_identity(request):

    if request.method == "POST":

        user_mobile = request.POST.get("userMobile","")
        sso_identity = request.POST.get("ssoIdentity","")

        #1:用户手机号不能为空！;2:手机号位数输入错误，请重新输入！;3:手机号格式输入错误，请重新输入！;4:正常
        mobile_result_tag = mobileNumberFormatValidity(user_mobile)
        # print ("mobile_result_tag",mobile_result_tag)

        if mobile_result_tag == 1:

            # return HttpResponse("用户手机号不能为空！")
            return JsonResponse({"status_code":10101,
                                 "message":"手机号不能为空！"})

        elif mobile_result_tag == 2:

            # return HttpResponse("手机号位数输入错误，请重新输入！")
            return JsonResponse({"status_code":10102,
                                 "message":"手机号位数输入错误，请重新输入！"})

        elif mobile_result_tag == 3:

            # return HttpResponse("手机号格式输入错误，请重新输入！")
            return JsonResponse({"status_code":10103,
                                 "message":"手机号格式输入错误，请重新输入！"})

        elif mobile_result_tag == 4:

            #查询账号状态返回用户id
            userId = talk_query_user_info_id_account_status_success(user_mobile)
            # print (userId)

            ssoidentity_result = ssoIdentity(sso_identity,userId)
            # print (ssoidentity_result.json())

            if ssoidentity_result == "httperror" or ssoidentity_result == "requesterror":

                return JsonResponse({"status_code": 10106,"message":"请求错误，请检查！"})

            else:

                try:

                    data_result = ssoidentity_result.json()['data']
                    # print (data_result)

                    if data_result == '角色变更，操作失败。操作失败，请稍后再试':

                        return JsonResponse({"status_code": 10104,"message":data_result,"result": data_result})

                    elif data_result == '标签限制,操作失败,请按右侧组合填写。':

                        return JsonResponse({"status_code": 10105,"message": "SSO身份修改失败","result": data_result})

                    else:

                        return JsonResponse({"status_code": 10200, "message": "SSO身份修改成功", "result": data_result})

                except:

                    return JsonResponse({"status_code": 10107, "message": "修改身份报错，请本地重新登录crm后台获取最新PHPSESSID信息"})


'''###############################################################################'''
#2020-08-20:张波修改
#ssoh5标签身份修改
@auth
def sso_h5(request):

    if request.method == "POST":

        user_mobile = request.POST.get("userMobile","")
        h5_label = request.POST.get("h5Label","")

        #1:用户手机号不能为空！;2:手机号位数输入错误，请重新输入！;3:手机号格式输入错误，请重新输入！;4:正常
        mobile_result_tag = mobileNumberFormatValidity(user_mobile)
        # print ("mobile_result_tag",mobile_result_tag)

        if mobile_result_tag == 1:

            # return HttpResponse("用户手机号不能为空！")
            return JsonResponse({"status_code":10101,
                                 "message":"手机号不能为空！"})

        elif mobile_result_tag == 2:

            # return HttpResponse("手机号位数输入错误，请重新输入！")
            return JsonResponse({"status_code":10102,
                                 "message":"手机号位数输入错误，请重新输入！"})

        elif mobile_result_tag == 3:

            # return HttpResponse("手机号格式输入错误，请重新输入！")
            return JsonResponse({"status_code":10103,
                                 "message":"手机号格式输入错误，请重新输入！"})

        elif mobile_result_tag == 4:

            #查询账号状态返回用户id
            userId = talk_query_user_info_id_account_status_success(user_mobile)
            # print (userId)

            if h5_label == '0' or h5_label == '1':

                sso_h5_result = ssoH5_modify(userId,h5_label)
                # print (sso_h5_result.json())

                if sso_h5_result.json()['data'][10:11] == '是':

                    return JsonResponse({"status_code": 10200,"message":"该学员h5标签修改成功！"})

                elif sso_h5_result.json()['data'][10:11]  == '否':

                    return JsonResponse({"status_code": 10200,"message":"该学员h5标签取消成功！"})