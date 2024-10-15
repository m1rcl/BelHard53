"""
Написать функцию printn() которая будет печатать переданный текст,
но при этом перед этим текстом выводить строку с номером отражающим
кокай раз по счету выполняется эта функция.

"""


def printn(user_input):
    if user_input:
        print(f"строка {counter} : {user_input}")


user_input = ' '
counter = 0
while user_input:
    user_input = input(
        f"Введите строку {counter} для отображения в консоли, либо оставьте пустой для выхода: ")
    counter = counter + 1
    printn(user_input)
