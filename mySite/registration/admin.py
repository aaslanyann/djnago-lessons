from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import CustomUser

class CustomUserInLine(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = 'CustomUser'

class CustomizedUserAdmin(UserAdmin):
    inlines = (CustomUserInLine, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
admin.site.register(CustomUser)