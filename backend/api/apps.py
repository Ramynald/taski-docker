"""Application configuration for api app."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Configuration for api application."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
