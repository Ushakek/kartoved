from django.contrib import admin

from notes.models import ModelNotes


@admin.register(ModelNotes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ['name', 'coordinates', 'user_profile']
