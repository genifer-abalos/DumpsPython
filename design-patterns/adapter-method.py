from abc import ABC
# we have two interfaces (abstract classes) Notification and Music
# Notification class has 2 types of alerts, sound_alert and beep_alert
# Music class has a music_alert
# we want to create an adapter so that we have a class that ...
# can implement the music_alert from Music class
# and beep_alert from Notification class
# Takeaway: We do this, instead of creating a whole new class say All_Notifs class
# and copying all the functions (which is not scalable in big projects)


class Notification(ABC):
    def __init__(self):
        pass

    def sound_alert(self):
        pass

    def beep_alert(self):
        pass


class Music(ABC):
    def __init__(self):
        pass

    def music_alert(self):
        pass


class NotificationAdapter(Music, Notification.beep_alert):
    def beep_alert(self):
        pass

    def music_alert(self):
        pass


if __name__ == '__main__':

    adapter = NotificationAdapter()
    adapter.beep_alert()
    adapter.music_alert()
