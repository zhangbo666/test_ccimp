
from django.urls import path
from ccimp_project_app import views

from ccimp_project_app.models.projectModels import Project

urlpatterns = [

    path('',views.project_manage),
    path('add_project/',views.add_project),
    path('edit_project/<int:pid>/',views.edit_project),
    path('delete_project/<int:pid>/',views.delete_project),
    path('search',views.project_search),

    # 接口
    path('get_edit_project_data/',views.get_edit_project_data),
    path('edit_save_project/',views.edit_save_project),
]