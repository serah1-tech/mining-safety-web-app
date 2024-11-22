from django.db import models

class HazardAlert(models.Model):
    location = models.CharField(max_length=255)  # MySQL equivalent: VARCHAR(255)
    description = models.TextField()  # MySQL equivalent: TEXT
    timestamp = models.DateTimeField(auto_now_add=True)  # MySQL equivalent: DATETIME with default CURRENT_TIMESTAMP

    def __str__(self):
        return f"Hazard at {self.location}"
