
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


    #修改账号状态
    path('user_info/account_status/', views.account_status),


    #修改手机号状态
    path('user_info/mobile_status/', views.mobile_status),


    #修改用户身份状态
    path('user_info/user_identity/', views.user_identity),


    #修改课程状态
    path('user_info/course_status/', views.course_status),

]