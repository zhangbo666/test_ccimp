from django.contrib import admin

# Register your models here.


from django.contrib import admin

from ccimp_systemSettings_app.models.WebConfigModels import WebConfig

class WebConfigAdmin(admin.ModelAdmin):

    list_display = ['nameConfig','keyConfig','valueConfig','describeConfig','create_time','update_time']

    search_fields = ['nameConfig','keyConfig']

admin.site.register(WebConfig,WebConfigAdmin)