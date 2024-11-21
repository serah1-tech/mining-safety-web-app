from django.contrib import admin
from .models import SafetyTip

class SafetyTipAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

admin.site.register(SafetyTip, SafetyTipAdmin)
