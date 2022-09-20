from django.contrib import admin
from .models import NetworkMobile, Network


# Register your models here.

class NetworkAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


class NetworkMobilesAdmin(admin.ModelAdmin):
    list_display = ('operator', 'x', 'y', 'coordinate_x', 'coordinate_y', 'g2', 'g3', 'g4')
    search_fields = ['coordinate_x', 'coordinate_y', ]


admin.site.register(Network, NetworkAdmin)
admin.site.register(NetworkMobile, NetworkMobilesAdmin)
