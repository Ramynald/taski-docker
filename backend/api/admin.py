"""Admin configuration for Task model."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Admin panel settings for Task model."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
