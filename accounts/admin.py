from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin

from accounts.models import (Owner, Profile)


# OwnerProfile
class OwnerInline(admin.StackedInline):
    model = Owner
    can_delete = False


# UserProfile
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline, OwnerInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
