
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
    path('user_info/get_user_sms_connent/',views.get_user_sms_connent)


]