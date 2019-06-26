from django.contrib import admin

# Register your models here.


from ccimp_project_app.models import Project


class ProjectAdmin(admin.ModelAdmin):

        list_display = ['name','describe','status','create_time','update_time']

        search_fields = ['name']

        list_filter = ['status']


admin.site.register(Project,ProjectAdmin)