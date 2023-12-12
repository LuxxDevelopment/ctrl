from ctrl.alerts import desktopActionMessage
from winotify import audio
desktopActionMessage("TEST", "HEY", "P:\Phyton\ctrl\src\ctrl\img\icon.png", "short", "Start CMD", "C:\WINDOWS\system32\cmd.exe", audio.LoopingAlarm10, False)