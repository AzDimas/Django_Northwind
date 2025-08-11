from django.contrib import admin
from django.contrib.auth.models import User
from .models import Role, Profile

# Register your models here.

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('permissions',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    filter_horizontal = ('roles',)
