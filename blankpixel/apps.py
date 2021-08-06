from django.apps import AppConfig


class BlankpixelConfig(AppConfig):
    name = 'blankpixel'
    def ready(self):
        import blankpixel.signals