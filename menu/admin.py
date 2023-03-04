from django.contrib import admin
from .models import Menu, MenuItem

class ItemInline(admin.StackedInline):
    model = MenuItem
    fields = ('slug',)
    show_change_link = True
    extra = 0
    
class MenuAdmin(admin.ModelAdmin):
    inlines = (ItemInline,)

class ItemAdmin(admin.ModelAdmin):
    inlines = (ItemInline,)



admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, ItemAdmin)