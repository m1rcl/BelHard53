'''
1. Написать функцию которая принимает некоторые данные пользователя 
с помощью (**kwargs). Если есть данные с именем(name) или фамилией(surname) 
или возрастом(age), распечатать информацию о пользователе используя присутствующие 
из этих трех параметров, иначе вывести сообщение о том, что нужных данных нет.
'''


def user_info(**kwargs):
    return (f"Имя пользователя: {kwargs["name"] if "name" in kwargs.keys() else "данных нет"},\n"
            f"фамилия пользователя: {
                kwargs["surname"] if "surname" in kwargs.keys() else "данных нет"},\n"
            f"возраст пользователя: {kwargs["age"] if "age" in kwargs.keys() else "данных нет"}")


print(user_info(name="John", surname="Doe"))
