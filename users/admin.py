from django.contrib import admin
from django.contrib.auth.models import User

from users.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'user_status', 'available_for_work', 'phone']
