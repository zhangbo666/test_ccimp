
from django.urls import path
from ccimp_tool_app import views

urlpatterns = [

    #售卖下单
    path('sale_order/',views.sale_order),
    # path('edit_project/<int:pid>/',views.edit_project),
    # path('delete_project/<int:pid>/',views.delete_project),
    # path('search',views.project_search),

    # 售卖下单接口
    path('sale_order/get_package_detail/',views.get_package_detail),
    path('sale_order/order_pay_success/',views.order_pay_success),
    path('sale_order/get_order_detail/',views.get_order_detail),
    path('sale_order/process_order/',views.process_order),
    path('sale_order/get_order_on_detail/',views.get_order_on_detail),


    #学员信息
    path('user_info/',views.user_info),


    #学员信息接口
    path('user_info/get_userinfo_detail/',views.get_userinfo_detail),


    #手机短信内容接口
    path('user_info/get_user_sms_connent/',views.get_user_sms_connent),


    # 给学员添加次卡
    path('user_addpoint/', views.add_user_point),


    #修改用户昵称
    path('user_info/user_nick_name/', views.user_nick_name),


    #注册新用户,判断用户是否注册
    path('user_info/register_mobile_check/', views.register_mobile_check),


    #新账号注册
    path('user_info/post_registerInfo/', views.post_registerinfo_mobile),


    #修改账号状态
    path('user_info/account_status/', views.account_status),


    #修改手机号状态
    path('user_info/mobile_status/', views.mobile_status),


    #修改用户身份状态
    path('user_info/user_identity/', views.user_identity),


    # 2020-07-05:张波修改
    #修改课程状态
    # path('user_info/course_status/', views.course_status),


    # 2020-07-05:张波修改
    #获取用户约课记录
    path('user_info/get_user_appoint_record/', views.get_user_appoint_record),


    # 2020-07-11:张波修改--获取数据方法二合一，暂时屏蔽这个方法
    #获取约课记录list
    # path('user_info/api/getAppointRecordListData', views.getAppointRecordListData),


    # 2020-07-05:张波修改
    #约课课程状态修改
    path('user_info/api/appoint_record', views.appoint_record),


    #公开课
    path('open_class/', views.open_class),
    path('open_class/open_class_add/',views.open_class_add),
    # path('open_class/open_class_appoint/', views.open_class_appoint),

    #获取公开课老师list
    path('open_class/api/getSelectTeacherData', views.getSelectTeacherData),

    #获取公开课教材list
    path('open_class/api/getSelectTextBookData', views.getSelectTextBookData),

]