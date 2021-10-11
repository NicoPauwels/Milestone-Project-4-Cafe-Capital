from django.contrib import admin
from .models import Category, Item

class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'item',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('item',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)