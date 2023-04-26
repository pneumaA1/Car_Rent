from django.contrib import admin
from django.utils.safestring import mark_safe

from webapp.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Car model.

    Displays and allows admin management of Car objects.
    Provides a preview of the Car's photo in the admin interface.
    """
    fields = (
    'title', 'door_count', 'seats_count', 'transmission', 'rating', 'price',
    'photo', 'is_main', 'preview_photo',)
    readonly_fields = ('preview_photo',)
    list_display = (
    'pk', 'title', 'door_count', 'seats_count', 'transmission', 'rating',
    'is_main')
    list_display_links = ('title',)
    list_editable = ('is_main',)
    list_filter = (
    'door_count', 'seats_count', 'transmission', 'rating', 'is_main',)
    search_fields = ('title',)

    def preview_photo(self, obj):
        """
        Returns HTML markup for displaying a preview of the Car's photo in the admin interface.
        Uses the mark_safe function to allow rendering of HTML in the admin interface.
        """
        return mark_safe(f'<img src="{obj.photo.url}"width="150">')
