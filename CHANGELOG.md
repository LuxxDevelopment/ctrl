# CHANGELOG

-----

## Client:
### 11.12.2023 -- 22:25
Added Windows Desktop Messages in ```` ./src/client/ctrl/alerts.py```` \
USAGE: 

`````python
    from ctrl.alerts import desktopActionMessage
    from winotify import audio
    desktopMessage("ALERT", "Couldn't reach Command server!", "short", audio.LoopingAlarm10, False)
    desktopActionMessage("ALERT", "Couldn't reach Command server!", "P:\Phyton\ctrl\src\ctrl\img\icon.png","short","OPEN CONSOLE","https://youtube.com/", audio.LoopingAlarm10, False)
`````

Added Discord Webhook logs in `./src/client/ctrl/APIS/discord_logger.py`\
USAGE:

`````python
    from ctrl.APIS.discord_logger import logMessage
    from ctrl.APIS.discord_logger import sendFile
    url = "[REDACTED]"
    logMessage(url, title="This is a Test Message from CTRL - MANAGEMENT", description="Just a Plain ol Test message", color_hex="#FFFFFF")
    sendFile(url, title="This is a Test Message from CTRL - MANAGEMENT", description="Just a Plain ol Test message", file_name="log.png", file_path="P:\Phyton\ctrl\src\ctrl\img\icon.png", color_hex="#FFFFFF")
`````

Added tcp Chatroom in `./src/client/ctrl/chatroom.py`\
USAGE:
`````python
    NOT JET WORKING    
`````

## Server:
### 11.12.2023 -- 22:25
Added tcp Chatroom server in `./src/server/chatroom_Server.py`\
USAGE:
`````python
    NOT JET WORKING    
`````