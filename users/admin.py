from django.contrib import admin
from django.contrib.auth.models import User

from users.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass
