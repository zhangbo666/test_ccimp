
from django.urls import path

from ccimp_permission_app import views


urlpatterns = [

    path('',views.permission_manage),
    path('class/',views.permission_class),
    path('class/add_permissionClass/',views.add_permissionClass),
    path('class/edit_permissionClass/<int:pclass_id>/',views.edit_permissionClass),
    # path('delete_project/<int:pid>/',views.delete_project),
    # path('search',views.project_search),

]