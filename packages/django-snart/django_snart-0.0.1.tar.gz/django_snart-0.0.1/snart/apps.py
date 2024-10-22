from django.apps import AppConfig


class SnartAppConfig(AppConfig):
    name = "snart"
    verbose_name = "Snart"

    def ready(self):
        pass
