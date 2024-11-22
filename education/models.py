
from django.db import models

class SafetyLesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    duration = models.IntegerField(null=True, blank=True)  # Add duration if necessary
    start_date = models.DateField(null=True, blank=True)    # Add start_date if necessary
    end_date = models.DateField(null=True, blank=True)      # Add end_date if necessary
    description = models.TextField(null=True, blank=True)   # Add description field (if necessary)

    def __str__(self):
        return self.title


