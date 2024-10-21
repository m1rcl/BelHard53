
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # определили tcp/ip

# HOST = ('192.168.0.31', 7777)
HOST = ('127.0.0.1', 7777)

sock.bind(HOST)
sock.listen()
print('Слушаю....')

# HTTP 
# GET /project1/test1/ HTTP/1.1 - первая строка определяющая что это http - 3 параметра разделенные пробелом (тип путь протокол)
# Host: some.ru - 2я и последующие строки заголовки

path = ''

while 1:
    conn, addr = sock.accept() # зависаем в ожидании
    data = conn.recv(1024).decode() # принимаем данные по 1 КБайту
    # path = data.split('\n')[0].split()[1] # получаем path из 1ой строки http
    if path == '/test1/':
        print('Запускаю тест1')        
    
    else:    
        print(data)
        
    
