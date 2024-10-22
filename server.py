import socket
from _thread import *
import threading
# Список для хранения всех подключенных клиентов
clients = []

# Поток для обработки каждого клиента
def client_thread(conn, addr):
    print(f"New connection from {addr}")
    conn.send("Welcome to the chat room!\n".encode())

    while True:
        try:
            # Получаем сообщение от клиента
            message = conn.recv(1024).decode()
            if not message:
                break
            
            # Отправляем сообщение всем клиентам, кроме отправителя
            broadcast(message, conn)
        except:
            break

    # Закрываем соединение
    conn.close()
    clients.remove(conn)

# Отправка сообщения всем клиентам
def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message.encode())
            except:
                client.close()
                clients.remove(client)


server = socket.socket()
hostname = socket.gethostname()
port = 12345
server.bind((hostname, port))
server.listen(5)

print("Server running...")
    
while True:
    conn, addr = server.accept()
    clients.append(conn)
        
        # Запускаем новый поток для каждого подключенного клиента
    start_new_thread(client_thread, (conn, addr))


