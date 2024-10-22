from notifications.management.commands.delete_old_notifications import Command

def delete_old_notifications():
    Command().handle()