from django.apps import AppConfig


class MonitoringConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "monitoring"

    def ready(self) -> None:
        # Evita iniciar a thread duplicada no processo pai do autoreload.
        import os

        if os.environ.get("RUN_MAIN") == "true" or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
            from .serial_reader import SERIAL_READER

            SERIAL_READER.start()
