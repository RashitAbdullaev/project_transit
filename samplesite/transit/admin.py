from django.contrib import admin

from .models import Request


class UserAdmin(admin.ModelAdmin):
    list_display = ('user',)


class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'direction', 'type', 'time', 'weight', 'measure_name')
    list_display_links = ('name', 'direction', 'type', 'time', 'weight', 'measure_name')


admin.site.register(Request, RequestAdmin,)
