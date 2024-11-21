from django.db import models

class SafetyTip(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()  # This field stores the content of the safety tip

    def __str__(self):
        return self.title
