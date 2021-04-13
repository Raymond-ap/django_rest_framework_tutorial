from django.contrib import admin
from .models import *


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')
    search_fields = ('title',)
