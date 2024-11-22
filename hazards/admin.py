from django.contrib import admin
from .models import HazardAlert

@admin.register(HazardAlert)
class HazardAlertAdmin(admin.ModelAdmin):
    list_display = ('location', 'timestamp', 'description')  # Display these fields in the admin list view
    list_filter = ('timestamp',)  # Add a filter by timestamp
    search_fields = ('location',)  # Enable searching by location
