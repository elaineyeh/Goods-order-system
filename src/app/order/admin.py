from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Order, OrderGood


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'date'
    )
    list_display_links = (
        'id',
    )
    list_filter = (
        'user',
        'date'
    )

@admin.register(OrderGood)
class OrderGoodAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order',
        'good',
        'amount'
    )
    list_display_links = (
        'id',
    )
    list_filter = (
        'order',
        'good'
    )
