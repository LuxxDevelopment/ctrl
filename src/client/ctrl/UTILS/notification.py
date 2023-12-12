import time
from winotify import Notification, audio


def desktopMessage(title="NOTHING", msg="Just a message with nothing init",
                   icon_path="P:\Phyton\ctrl\src\ctrl\img\icon.png", duration="short", sound=audio.Silent, loop=False):
    toast = Notification(app_id="CTRL - MANAGEMENT",
                         icon=icon_path,
                         title=title,
                         msg=msg,
                         duration=duration)

    toast.set_audio(sound, loop=loop)
    toast.show()


def desktopActionMessage(title="NOTHING", msg="Just a message with nothing init",
                         icon_path="P:\Phyton\ctrl\src\ctrl\img\icon.png", duration="short", button_label=None,
                         button_launch="https://youtube.com/", sound=audio.Silent, loop=False):
    toast = Notification(app_id="CTRL - MANAGEMENT",
                         icon=icon_path,
                         title=title,
                         msg=msg,
                         duration=duration)

    toast.add_actions(label=button_label, launch=button_launch)
    toast.set_audio(sound, loop=loop)
    toast.show()


# desktopMessage("ALERT", "Couldn't reach Command server!", "short", audio.LoopingAlarm10,
# False) desktopActionMessage("ALERT", "Couldn't reach Command server!", "P:\Phyton\ctrl\src\ctrl\img\icon.png",
# "short","OPEN CONSOLE","https://youtube.com/", audio.LoopingAlarm10, False)


def ctkMessageBox():
    pass
