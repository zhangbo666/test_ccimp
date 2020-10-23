
from django.urls import path

from ccimp_links_app import views



urlpatterns = [

    # 友情链接
    path('',views.links_manage),

]