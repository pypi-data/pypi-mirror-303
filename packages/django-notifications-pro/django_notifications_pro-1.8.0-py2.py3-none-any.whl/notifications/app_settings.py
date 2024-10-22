import importlib
from django.conf import settings

USER_SETTINGS = getattr(settings, "DJANGO_NOTIFICATIONS_CONFIG", None)


DEFAULTS = {
    'PAGINATE_BY': 20,
    'USE_JSONFIELD': False,
    'SOFT_DELETE': False,
    'NUM_TO_FETCH': 10,
    'CACHE_TIMEOUT': 2,

    # Custom settings
    'USE_EXPO_NOTIFICATIONS': False,
    'EXPO_APP_ID': '',
    'AUTO_DELETE_NOTIFICATIONS': False,
    'NOTIFICATIONS_DELETE_DAYS': 30,
}


class APISettings:
    def __init__(self, user_settings=None, defaults=None):
        self.defaults = defaults
        self._user_settings = self.__check_user_settings(user_settings) \
            if user_settings else {}
        self.__check_expo_notifications()  
        self.__check_auto_delete_notifications()

    def __check_user_settings(self, user_settings):
        for setting in user_settings:
            if setting not in self.defaults:
                raise RuntimeError(
                    f"The {setting} setting is not a valid setting for DJANGO_NOTIFICATIONS_CONFIG.")

        return user_settings

    def get_user_setting(self, attr):
        try:
            return self._user_settings[attr]
        except KeyError:
            return self.defaults[attr]
        
    def __check_expo_notifications(self):
        """
        If 'USE_EXPO_NOTIFICATIONS' is enabled, verify if 'exponent_server_sdk' is installed.
        """
        if self.get_user_setting('USE_EXPO_NOTIFICATIONS'):
            expo_sdk_installed = importlib.util.find_spec("exponent_server_sdk") is not None
            if not expo_sdk_installed:
                raise ImportError(
                    "The package 'exponent_server_sdk' is not installed. Please install it by running 'pip install django-notifications-pro[expo]'."
                )
            
    def __check_auto_delete_notifications(self):
        """
        If 'AUTO_DELETE_NOTIFICATIONS' is enabled, verify if 'django-crontab' is installed.
        """
        if self.get_user_setting('AUTO_DELETE_NOTIFICATIONS'):
            cron_installed = importlib.util.find_spec("django_crontab") is not None
            if not cron_installed:
                raise ImportError(
                    "The package 'django_crontab' is not installed. Please install it by running 'pip install django-notifications-expo-go[cron]'."
                )



api_settings = APISettings(USER_SETTINGS, DEFAULTS)
