from django.apps import AppConfig


class PetloversConfig(AppConfig):
    """ It is a class that receives the Django App and allows to modify Petlovers

    Args:
        AppConfig (AppConfig): The AppConfig class used to configure the application has a path class attribute, which is the absolute directory path Django will use as the single base path
    """   
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'petlovers'
