from django.contrib import admin

from notes.models import ModelNotes


@admin.register(ModelNotes)
class NotesAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'coordinates',
        'work',
        'description',
        'photo',
        'marker',
        'user_profile',
    )
    list_display = ['name', 'coordinates', 'user_profile']
