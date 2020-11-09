
from django.urls import path,re_path

from ccimp_systemSettings_app import views



urlpatterns = [

    # 系统配置文件链接
    path('Admin/webConfig',views.systemConfig_manage),

    # 系统配置文件添加
    path('Admin/webConfig/add', views.add_webConfigs),

    # 系统配置文件修改
    # re_path(r'Admin/webConfig/edit/\\?id([\=])(?P<wCid>\d+)/$', views.edit_webConfigs,name='edit_webConfigs'),
    path('Admin/webConfig/edit/id=<int:wCid>/', views.edit_webConfigs),

    # 获取配置文件数据
    path('Admin/webConfig/get_edit_webConfig_data', views.get_edit_webConfig_data),

    # 配置文件数据保存
    path('Admin/webConfig/edit_save_webConfig', views.edit_save_webConfig),

    # 配置文件搜索
    path('Admin/webConfig/webConfig_search', views.webConfig_search),

]