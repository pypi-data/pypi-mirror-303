from django.core.management.base import BaseCommand
from django.utils import timezone
from notifications.app_settings import app_settings
from datetime import timedelta
from swapper import load_model


Notification = load_model('notifications', 'Notification')


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        auto_delete = app_settings.get('AUTO_DELETE_NOTIFICATIONS', False)
        delete_days = app_settings.get('NOTIFICATIONS_DELETE_DAYS', 30)  

        if not auto_delete:
            self.stdout.write("Auto delete notifications is disabled.")
            return

        self.delete_old_notifications(delete_days)

    def delete_old_notifications(self, delete_days):
        threshold_date = timezone.now() - timedelta(days=delete_days)
        
        try:
            deleted, _ = Notification.objects.filter(timestamp__lte=threshold_date).delete()
            if deleted:
                self.stdout.write(f"Deleted {deleted} old notifications.")
            else:
                self.stdout.write("No notifications to delete.")
        except Exception as e:
            self.stderr.write(f"An error occurred while deleting notifications: {e}")