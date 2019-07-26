from django.contrib import admin

from ccimp_project_app.models.projectModels import Project


class ProjectAdmin(admin.ModelAdmin):

    list_display = ['name','describe','status','create_time','update_time']

    search_fields = ['user_name']


admin.site.register(Project,ProjectAdmin)