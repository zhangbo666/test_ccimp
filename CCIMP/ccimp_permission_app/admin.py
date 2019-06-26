from django.contrib import admin

from ccimp_permission_app.models.permissionClassModels import PermissionClass


class PermissionClassAdmin(admin.ModelAdmin):

    list_display = ['permission_chinese_name','permission_english_name','permission_options','create_time','update_time']

admin.site.register(PermissionClass,PermissionClassAdmin)