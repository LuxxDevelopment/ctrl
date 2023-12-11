import socket
import threading
from rich.console import Console
import sys

console = Console()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8092))

nickname = console.input("[yellow][?][/yellow] Enter anew Nickname: ")


def receive():
    while True:
        try:
            message = client.recv(1024).decode("ISO-8859-1")
            if message == "NICK":
                client.send(nickname.encode("ISO-8859-1"))
            else:
                console.print(message)
        except:
            console.print("[bold red]![/bold red] A error has occurred")
            client.close()
            sys.exit(0)


def write():
    while True:
        message = input("")
        message = f'{nickname}: {message}'
        client.send(message.encode())


receive_thread = threading.Thread(target=receive).start()
write_thread = threading.Thread(target=write).start()
