from django.contrib import admin

from accounts.models import Member


@admin.register(Member)
class Member(admin.ModelAdmin):
    list_display = ['id', 'phone_number']
