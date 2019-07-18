
from django.urls import path

from ccimp_permission_app import views


urlpatterns = [

    # 用户权限
    path('',views.permission_manage),
    path('edit_permission/<int:uid>/', views.edit_permission),
    path('edit_permission/get_edit_permission/<int:uid>/', views.edit_permission),

    # 权限管理
    path('class/',views.permission_class),
    path('class/add_permissionClass/',views.add_permissionClass),
    path('class/edit_permissionClass/<int:pclass_id>/',views.edit_permissionClass),
    # path('delete_project/<int:pid>/',views.delete_project),
    # path('search',views.project_search),


    # 接口
    path('class/edit_permissionClass/get_edit_permissionClass/',views.get_edit_permissionClass),
    path('class/save_permissionClass/',views.save_permissionClass),

]