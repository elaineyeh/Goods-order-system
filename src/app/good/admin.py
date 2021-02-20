from django.contrib import admin

from .models import Good

@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'stock',
        'date'
    )
    list_display_links = (
        'id',
    )
    list_filter = (
        'price',
        'date'
    )
