'''
1. Написать функцию, которая получает строку и возвращает обработанную строку.
Если строка уже заканчивается числом, это число следует увеличить на 1.
Если строка не заканчивается числом, к исходной строке следует добавить число 1.
Если в числе есть ведущие нули, следует учитывать количество цифр.
Примеры:
foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100
'''


def inc_num_in_string(some_str):
    if some_str.isalpha():
        output_string = some_str + "1"
        return output_string

    for item in range(len(some_str)):
        if some_str[item].isdigit():
            num_in_string = some_str[item:len(some_str)+1]
            output_string = some_str[0:item] + \
                str(int(num_in_string) + 1).zfill(len(num_in_string))
            return output_string


user_input = input("Введите строку: ")
inc_num_in_string(user_input)
print(inc_num_in_string(user_input))
