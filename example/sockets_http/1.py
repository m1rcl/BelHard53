
import socket




def send_file(file_name, conn):
    try:
        with open(file_name.lstrip('/'), 'rb') as f:                   
            print(f"send file {file_name}")
            conn.send(OK)
            conn.send(HEADERS)
            conn.send(f.read())
            
    except IOError:
        print('нет файла')
        conn.send(ERR_404)
        
        
def is_file(path):        
    if path[-4:] in ['.jpg','.png','.gif', '.ico', '.txt'] or path[-5:] in ['.html']:
        return True
    return False
       

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # определили tcp/ip

# HOST = ('192.168.0.31', 7777)
HOST = ('127.0.0.1', 7777)
# HOST = ('192.168.100.6', 7771)

sock.bind(HOST)
sock.listen()


# HTTP 
# GET /project1/test1/ HTTP/1.1 - первая строка определяющая что это http - 3 параметра разделенные пробелом (тип путь протокол)
# Host: some.ru - 2я и последующие строки заголовки
# 2 пустые строки
# служебные данные

path = ''

OK = b'HTTP/1.1 200 OK\n'
HEADERS = b"Host: some.ru\nHost1: some1.ru\n\n"
ERR_404 = b'HTTP/1.1 404 Not Found\n\n'

while 1:    
    print('Listen....')
    conn, addr = sock.accept() # зависаем в ожидании  
    data = conn.recv(4096).decode() # принимаем данные по 4 КБайт 
    print(data)   
    # data = ''  
    # while 1:
    #     rec = conn.recv(2).decode() # принимаем данные по 4 КБайт    
    #     if not rec:
    #         break
    #     data += rec
    
    
        
    
    try:
        path = data.split('\n')[0].split()[1] # получаем path из 1ой строки http                        
        if is_file(path):
            send_file(path, conn) #можно  запросить любой файл html или картинку
        else:
            print(f'no file {print(path)}- send tested file')    
            send_file('1.html', conn)
            
    except:
        conn.send(b'no http')
        
    conn.close()
        
    
