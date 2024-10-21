import socket

sock = socket.socket()

HOST = ('127.0.0.1', 7777)

sock.connect(HOST) # соединяемся с сервером указывая его адрес и порт

sock.send('1234567890'.encode('utf-8')) # отправляем данные кодируя в байтовое представление
# sock.send(b'1234567890') # или так сразу в байтовом представлении