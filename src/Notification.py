from User import User

class Notification:
    def __init__(self, notification_type):
        self._type = notification_type
        self._user = User()
        pass

    def notify_user(self, user):
        pass
