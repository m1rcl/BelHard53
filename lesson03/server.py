'''
написать приложение-сервер используя модуль socket работающее в домашней
локальной сети.
Приложение должно принимать данные с любого устройства в сети отправленные
или через программу клиент или через браузер
    - если данные пришли по протоколу http создать возможность след.логики:
        - если путь содержит /test/<int>/ вывести сообщение - тест с номером int запущен

        - если путь содержит message/<login>/<text>/ вывести в консоль сообщение
            "{дата время} - сообщение от пользователя {login} - {text}"

        - во всех остальных случаях вывести сообщение:
            "пришли неизвестные  данные по HTTP - путь такой то"


    - если данные пришли НЕ по протоколу http создать возможность след.логики:
        - если пришла строка формата "command:reg; login:<login>; password:<pass>"
            - выполнить проверку:
                login - только латинские символы и цифры, минимум 6 символов
                password - минимум 8 символов, должны быть хоть 1 цифра
            - при успешной проверке:
                1. вывести сообщение:
                    "{дата время} - пользователь {login} зарегистрирован"
                2. добавить данные пользователя в список/словарь
            - если проверка не прошла вывести сообщение:
                "{дата время} - ошибка регистрации {login} - неверный пароль/логин"

        - если пришла строка формата "command:signin; login:<login>; password:<pass>"
            выполнить проверку зарегистрирован ли такой пользователь:

            при успешной проверке:
                1. вывести сообщение:
                    "{дата время} - пользователь {login} произведен вход"

            если проверка не прошла вывести сообщение
                "{дата время} - ошибка входа {login} - неверный пароль/логин"

        - во всех остальных случаях вывести сообщение:
            "пришли неизвестные  данные - <присланные данные>"


'''


import datetime
import re
import socket

HOST = ('127.0.0.1', 7777)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(HOST)
server.listen()
users_login_db = {}

while True:
    print('Слушаю')
    conn, addr = server.accept()
    data = conn.recv(1024).decode('utf-8')
    path = data.split('\n')[0].split()[1]
    path_list = path.strip('/').split('/')

    if data.split('\n')[0].split()[2].startswith('HTTP'):
        if path_list[0] == 'test' and path_list[1].isdigit():
            print(f"тест с номером {path_list[1]} запущен")
        elif path_list[0] == 'message':
            print(f"{datetime.datetime.now()
                     } - сообщение от пользователя {path_list[1]} - {path_list[2]}")
        else:
            print(f"пришли неизвестные данные по HTTP - {path}")
    else:
        if path_list[0].startswith('command:'):
            command = path_list[0].lstrip('command:')
            if command == 'reg':
                if re.search(r'[a-zA-Z0-9]{6,}', path_list[1].lstrip('login:')) and re.search(r'(?=.*\d)[A-Za-z0-9]{8,}', path_list[2].lstrip('password:')):
                    print(f"{datetime.datetime.now()
                             } - пользователь {path_list[1].lstrip('login:')} зарегистрирован")
                    users_login_db.update({path_list[1].lstrip(
                        'login:'): path_list[2].lstrip('password:')})
                    print(users_login_db)
                else:
                    print(f"{datetime.datetime.now()
                             } - ошибка регистрации {path_list[1].lstrip('login:')} - неверный пароль/логин")
            if command == 'signin':
                print(users_login_db)
                print(users_login_db.get(path_list[1].lstrip('login:')))
                if users_login_db.get(path_list[1].lstrip('login:')) == path_list[2].lstrip('password:'):
                    print(f"{datetime.datetime.now()
                             } - пользователь {path_list[1].lstrip('login:')} произведен вход")
                else:
                    print(f"{datetime.datetime.now()
                             } - ошибка входа {path_list[1].lstrip('login:')} - неверный пароль/логин")
        else:
            print(f"пришли неизвестные данные - {path}")
