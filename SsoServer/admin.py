from django.contrib import admin
from .models import TestUser


class TestUserAdmin(admin.ModelAdmin):

    list_filter = ('username','password',)


admin.site.register(TestUser, TestUserAdmin)
