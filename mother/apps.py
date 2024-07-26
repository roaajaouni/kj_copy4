from django.apps import AppConfig


class MotherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mother'
    def ready(self):
        import mother.signals
