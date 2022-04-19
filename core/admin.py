from django.contrib import admin

from core.models import UserRegistrationRequest


@admin.register(UserRegistrationRequest)
class RequestRegistration(admin.ModelAdmin):
    list_display = ('username', 'userfullname', 'email', 'phone')
    list_display_links = ('username',)
    search_fields = ('phone', 'email')

    actions = ('register',)

    def register(self, request, queryset, *args):
        for user in queryset:
            user.register()

    register.short_description = 'Зарегистрировать пользователей'
