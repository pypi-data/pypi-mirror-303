from swapper import swappable_setting
from django.db import models
from notifications.signals import notify
from notifications.app_settings import api_settings as settings


from .base.models import AbstractNotification  # noqa


class Notification(AbstractNotification):

    class Meta(AbstractNotification.Meta):
        abstract = False
        swappable = swappable_setting('notifications', 'Notification')
    
    def naturalday(self):
        """
        Shortcut for the ``humanize``.
        Take a parameter humanize_type. This parameter control the which humanize method use.
        Return ``today``, ``yesterday`` ,``now``, ``2 seconds ago``etc. 
        """
        from django.contrib.humanize.templatetags.humanize import naturalday
        return naturalday(self.timestamp)

    def naturaltime(self):
        from django.contrib.humanize.templatetags.humanize import naturaltime
        return naturaltime(self.timestamp)     
    


if settings.get_user_setting('USE_EXPO_NOTIFICATIONS'):
    from notifications.expo_utils import expo_push_notification_handler
    class ExpoToken(models.Model):
        token = models.CharField(max_length=200)
        user = models.ForeignKey(
            "users.User", on_delete=models.CASCADE, related_name="expo_tokens"
        )
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.user} - {self.token}"


    notify.connect(
        expo_push_notification_handler, dispatch_uid="expo_push_notification_handler"
    )
