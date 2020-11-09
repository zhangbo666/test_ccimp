#!/usr/bin/python
#encoding:utf-8

"""CCIMP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from ccimp_user_app import views

urlpatterns = [

    # admin后台
    path('admin/', admin.site.urls),

    # 用户app
    path('',views.index),
    path('index/', views.index),

    path('login_ccimp/', views.login_ccimp),
    path('register_ccimp/',views.register),

    path('logout/',views.logout),

    # 项目管理app
    path('project/',include('ccimp_project_app.urls')),

    # 权限用户与权限分类管理app
    path('permission/',include('ccimp_permission_app.urls')),

    # 友情链接
    path('links/',include('ccimp_links_app.urls')),

    # 工具管理app
    path('tool/',include('ccimp_tool_app.urls')),

    # 系统设置app
    path('systemSettings/', include('ccimp_systemSettings_app.urls')),

]









