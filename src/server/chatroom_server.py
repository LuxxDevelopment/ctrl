import threading
import socket
from rich.console import Console

console = Console()

host = "127.0.0.1"  # At this point still localhost for testing
port = 8092

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def broadcastMessage(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            index = clients.index(client)
            nickname = nicknames[index]
            message = client.recv(1024)
            broadcastMessage(f"{message}")
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcastMessage(f"{nickname} left the chat!".encode('ISO-8859-1'))
            console.print(f"{nickname} left the chat!")
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, addr = server.accept()
        client.send("NICK".encode("ISO-8859-1"))
        nickname = client.recv(1024).decode("ISO-8859-1")
        nicknames.append(nickname)
        clients.append(client)

        print(f"NEW CLIENT!\nAddress: {str(addr)}\nNickname: {str(nickname)}")
        broadcastMessage(f"{nickname} just joined the chat!".encode("ISO-8859-1"))
        client.send("Connected to the Chat room!".encode("ISO-8859-1"))

        thread = threading.Thread(target=handle, args=(client,)).start()


console.print("[bold green] SERVER RUNNING [/bold green]")
receive()
