from django.contrib import admin

from .models import Flat, Disliker



class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']
    list_filter = ['new_building']


class DislikeAdmin(admin.ModelAdmin):
    raw_id_fields = ['disliker', 'flat']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Disliker, DislikeAdmin)
