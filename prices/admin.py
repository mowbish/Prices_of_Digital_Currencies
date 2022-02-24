from django.contrib import admin

from django.contrib import admin
from .models import User, FileDetail


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email", "date_joined")
    search_fields = ('username', "first_name", "last_name", "email",)
    empty_value_display = '-empty-'
    ordering = ('date_joined',)


@admin.register(FileDetail)
class FileDetailAdmin(admin.ModelAdmin):
    list_display = ("user", "file", "upload_date")
    list_filter = ('upload_date',)
    date_hierarchy = 'upload_date'
    search_fields = ("file",)
    empty_value_display = '-empty-'
    ordering = ('upload_date',)

