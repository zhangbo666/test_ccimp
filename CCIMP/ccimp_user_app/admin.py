from django.contrib import admin

from ccimp_user_app.models.userModels import User
from ccimp_user_app.models.userPermissionModels import UserPermission


class UserPermissionAdmin(admin.ModelAdmin):

    list_display = ['permission_chinese_name','permission_english_name','permission_options','create_time','update_time']


admin.site.register(UserPermission,UserPermissionAdmin)



class UserAdmin(admin.ModelAdmin):

    list_display = ['user_name', 'password', 'real_name', 'mail','create_time']

    search_fields = ['user_name']


admin.site.register(User,UserAdmin)