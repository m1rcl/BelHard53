'''
Дан список [1,2,3,4,5,6,7,8,9]. Создать 3 копии этого списка
и с каждой выполнить след действия:
    - возвести каждый элемент во 2ю степень
    - прибавить 3 к каждому элементу значение которого является четным
    - элементы значения которого является
            четными - умножить на 2
            нечетным - умножить на 3

Использовать map и lambda.
'''


import copy


some_list = [1,2,3,4,5,6,7,8,9]
some_list_1 = copy.copy(some_list)
some_list_2 = copy.copy(some_list)
some_list_3 = copy.copy(some_list)

print(some_list)

# я предположил, что каждое из трех действий нужно выполнять со своей копий оригинала
some_list_1 = list(map(lambda item: item ** 2, some_list_1))
print(some_list_1)

some_list_2 = list(map(lambda item: (item+3) if item%2==0 else item, some_list_2))
print(some_list_2)

some_list_3 = list(map(lambda item: (item*2) if item%2==0 else (item*3), some_list_3))
print(some_list_3)
