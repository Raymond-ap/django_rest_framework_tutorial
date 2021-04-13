from django.db import models
from django.utils.text import slugify

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
    