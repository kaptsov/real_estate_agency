from django.contrib import admin

from .models import Flat, Disliker, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ['liked_by']


class DislikeAdmin(admin.ModelAdmin):
    raw_id_fields = ['disliker', 'flat']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Disliker, DislikeAdmin)
admin.site.register(Owner, OwnerAdmin)
