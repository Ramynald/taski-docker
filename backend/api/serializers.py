"""Serializers for api application."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model."""

    class Meta:
        """Meta settings for TaskSerializer."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
