from django.contrib import admin
from .models import Car

from django.contrib import admin


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    """Вывод полей в админке"""
    list_display = ('brand', 'vin', 'color', 'is_published')
    # list_display_links = ('brand', 'vin')
    search_fields = ('brand', 'vin')
    save_on_top = True


