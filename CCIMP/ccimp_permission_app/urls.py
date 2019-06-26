
from django.urls import path

from ccimp_permission_app import views


urlpatterns = [

    path('',views.permission_manage),
    path('add_permission/',views.add_permission),
    # path('edit_project/<int:pid>/',views.edit_project),
    # path('delete_project/<int:pid>/',views.delete_project),
    # path('search',views.project_search),

]