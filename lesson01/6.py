"""
*
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом.
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""


a1 = 2.0
a2 = 2
a3 = "name"
a4 = 27

print(a1, a2, a3, a4)

if all(type(item) is float for item in (a1, a2, a3, a4)):
    print("Все переменные дробные - ", True)

if any(type(item) is str for item in (a1, a2, a3, a4)):
    print("Хотя бы одна из переменных строка - ", True)

if any(all(type(item) is int for item in pair) for pair in ((a1, a3), (a2, a4), (a3, a4))):
    print("Хотя бы одна из пар переменных является целочисленным типом - ", True)
