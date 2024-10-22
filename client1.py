import socket
from _thread import *

def receive_messages(client):
    while True:
        try:
            # Получение сообщений от сервера
            message = client.recv(1024).decode()
            if not message:
                break
            print(message)
        except:
            print("An error occurred!")
            client.close()
            break


client = socket.socket()
hostname = socket.gethostname()
port = 12345
client.connect((hostname, port))

print("Connected to the chat room!")

    # Запускаем поток для получения сообщений
start_new_thread(receive_messages, (client,))

    # Основной цикл отправки сообщений на сервер
while True:
    message = input()
    if message.lower() == 'exit':
        break
    client.send(message.encode())

client.close()


