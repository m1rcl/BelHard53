"""

написать приложение-клиент используя модуль socket работающее в домашней 
локальной сети.
Приложение должно соединятся с сервером по известному адрес:порт и отправлять 
туда текстовые данные.

известно что сервер принимает данные следующего формата:
    "command:reg; login:<login>; password:<pass>" - для регистрации пользователя
    "command:signin; login:<login>; password:<pass>" - для входа пользователя
    
    
с помощью программы зарегистрировать несколько пользователей на сервере и произвести вход


"""


import socket

client = socket.socket()

HOST = ('127.0.0.1', 7777)

client.connect(HOST)

# client.send("GET /test/1/ HTTP/1.1".encode('utf-8'))
# client.send("GET /message/vasya_pupkin/hello/ HTTP/1.1".encode('utf-8'))
# client.send("GET /some/something_else/ HTTP/1.1".encode('utf-8'))

# client.send(
#    "GET /command:reg/login:vasya_pupkin/password:vasya123/ NOT_HTTP_PROTOCOL".encode('utf-8'))
client.send(
    "GET /command:signin/login:vasya_pupkin/password:vasya123/ NOT_HTTP_PROTOCOL".encode('utf-8'))
