from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as MyUserAdmin

class UserAdmin(MyUserAdmin):
    filter_horizontal = MyUserAdmin.filter_horizontal + ('kitty',)
