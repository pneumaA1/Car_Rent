from django.apps import AppConfig


class WebappConfig(AppConfig):
    """
    Configuration class for the 'webapp' Django app.

    This class defines the configuration settings for the 'webapp' app,
    including the default auto field for database models and the name of
    the app itself.

    Attributes:
        default_auto_field (str): The name of the field to use for the primary
            key for each model. This defaults to 'django.db.models.AutoField',
            but can be overridden with this setting if desired.
        name (str): The name of the Django app. This should match the name of
            the app directory, and will be used in various places throughout
            the project to refer to this app (e.g. in database table names,
            URL patterns, etc.).
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webapp'
