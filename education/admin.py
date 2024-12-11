from django.contrib import admin
from .models import Lesson

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url', 'created_at')  # Ensure these fields are valid

admin.site.register(Lesson, LessonAdmin)
