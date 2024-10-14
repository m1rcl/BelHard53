"""
Дан список пользователей след. формата:
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов.
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания.
Каждому пользователю с плохим логином вывести текст
"Уважаемый user_name, ваш логин user_login не является корректным."

"""


def password_check(user_record):
    for symb in user_record['login']:
        if not symb.isalnum() and not symb == '_':
            return True


users_list = [
    {"name": "Ivanov Ivan", "login": "ivanov_ivan", "password": "qwer"},
    {"name": "Petrovov Petr", "login": "petrov_petr", "password": "qwerty12345"},
    {"name": "Doe John", "login": "doe john", "password": "123"}

]

bad_password_list = list(filter(lambda user_record: len(user_record['password']) < 5, users_list))
for user in bad_password_list:
    print(f"Уважаемый {user['name']}, ваш пароль менее пяти симоволов.")

bad_login_list = list(filter(password_check, users_list))
for user in bad_login_list:
    print(f"Уважаемый {user['name']}, ваш логин '{user['login']}' не является корректным.")
