import socket

sock = socket.socket()

HOST = ('127.0.0.1', 7777)

sock.connect(HOST) # соединяемся с сервером указывая его адрес и порт

send_data = b"0123456789"

sock.sendall(send_data) # отправляем данные 
data = sock.recv(1024) # принимаем ответ
print(data.decode())


