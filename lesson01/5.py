'''

Дан списк:
['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
Для каждого элемента в списке
    - вывести на экран сначала номер элемента
    - сам элемент
    - символ данного элемента, соответствующий номеру его позиции в списке.
Образец:
1 - qwertyu - q
2 - asdfggh - s
3 - zxcvbnm - c
и так далее...


'''


some_list = ['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']

for item in some_list:
    print(f"{some_list.index(item)} - {item} - {item[some_list.index(item)]}")
