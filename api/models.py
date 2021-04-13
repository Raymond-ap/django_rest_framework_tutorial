from django.db import models

class Task(model.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
    