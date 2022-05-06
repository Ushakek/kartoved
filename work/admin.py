from django.contrib import admin

from work.models import WorkModel


@admin.register(WorkModel)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'executor']
    filter_horizontal = ['execution']
