from django.contrib import admin

from ccimp_user_app.models.userModels import User

class UserAdmin(admin.ModelAdmin):

    list_display = ['user_name','real_name','mail','permission_options','create_time','update_time']

    search_fields = ['user_name']


admin.site.register(User,UserAdmin)