from django.contrib import admin
from .models import App

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'date', 'time')
    search_fields = ('email', 'phone_number')
    date_hierarchy = 'date'