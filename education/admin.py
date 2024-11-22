from django.contrib import admin
from .models import SafetyLesson

@admin.register(SafetyLesson)
class SafetyLessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url')  # Display these fields in the admin list view
