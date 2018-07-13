# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math

a = [2, -5, 8, 9, -25, 25, 4]
new_a = []
for num in a:
    if num > 0:
        new_num = math.sqrt(num)
        if new_num == int(new_num):
            new_a.append(int(new_num))
print(new_a)
        

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)


days = ['', 'первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое',
        'восьмое', 'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
        'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестандцатое', 'семнадцатое',
        'восемнадцатое', 'девятнадцатое', 'двадцатое', 'двадцать первое', 'двадцать второе',
        'двадцать третье', 'двадцать четвертое', 'двадцать пятое', 'двадцать шестое',
        'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое', 'тридцатое', 'тридцать первое']
months = ['', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября',
          'октября', 'ноября', 'декабря']
date = '13.07.2018'
day, month, year = date.split('.')
day = int(day)
month = int(month)
year = int(year)
print(days[day], months[month], year, 'года')


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

n = int(input('Введите число: '))
rand_list = []
for _ in range(n):
    rand_list.append(random.randint(-100, 100))
print(rand_list)



# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

x = [1, 2, 4, 5, 6, 2, 5, 2]
first_x = set(x)
print(first_x)

second_x = []
for elem in x:
    if x.count(elem) == 1:
        second_x.append(elem)
print(second_x)




