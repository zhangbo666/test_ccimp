
from django.urls import path
from ccimp_tool_app import views

urlpatterns = [

    # path('',views.sale_manage),
    path('sale_order/',views.sale_order),
    # path('edit_project/<int:pid>/',views.edit_project),
    # path('delete_project/<int:pid>/',views.delete_project),
    # path('search',views.project_search),

    # 接口
    path('sale_order/get_package_detail/',views.get_package_detail),
    path('sale_order/order_pay_success/',views.order_pay_success),
]