"""
Дан словарь наблюдения за температурой
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}.
Отсортировать словарь по температуре в порядке возрастания и обратно.

"""


temperature_dict = {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}

sorted_temperature_dict = dict(sorted(temperature_dict.items(), key=lambda item: item[1]))
print(sorted_temperature_dict)

reversed_temperature_dict = dict(sorted(temperature_dict.items(), key=lambda item: item[1], reverse=True))
print(reversed_temperature_dict)
