"""
Запросить любое число не менее 10.
Вывести на экран сумму квадратов каждой цифры составляющей это число.
Например: дано 236 => 2*2 + 3*3 + 6*6 = 49

"""


user_num = input("Введите любое число: ")
sum_of_digit = 0

for digit in user_num:
    sum_of_digit += float(digit)**2

print(sum_of_digit)
