from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

# signl fnction jo signal.py file mein create kiya us ko register krny k liya
def ready(self):
    import users.signals