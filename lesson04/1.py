"""
Написать программу-сервер принимающую hhtp запросы и 
отдающую в ответ html-файл или файл картинку указанный в пути запроса.
Если запрос на главную страницу - вернуть заголовок h2 - Главная страница.
Если файла нет - выдать ошибку 404

"""

import socket


def send_file(file_name, conn):
    try:
        with open("material\\" + file_name, "rb") as f:
            print(f"отправляем файл {file_name}")
            conn.send(OK)
            conn.send(HEADERS)
            conn.send(f.read())

    except IOError:
        print("нет файла")
        conn.send(ERR_404)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


HOST = ("127.0.0.1", 7777)

sock.bind(HOST)
sock.listen()

path = ""

OK = b"HTTP/1.1 200 OK\n"
HEADERS = b"Host: some.ru\n\n"
ERR_404 = b"HTTP/1.1 404 Not Found\n\n"

while 1:
    print("Слушаю....")
    conn, addr = sock.accept()
    data = conn.recv(4096).decode()

    try:
        path = data.split("\n")[0].split()[1].strip("/")
        if path:
            send_file(path, conn)
        else:
            send_file("main.html", conn)

    except:
        conn.send(b"no http")

    conn.close()
