'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы
 - остались только строки.
 - остался только логический тип.

'''


some_list = ['hello', -3, True, 3.14]
filtered_list = list(filter(lambda item: type(item) is str or type(item) is bool, some_list))
print(filtered_list)
