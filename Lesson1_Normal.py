# Задача 1

number = int(input('Введите число от 0 до 10: '))

while number > 0:
    if number < 10:
        number = number ** 2
        print(number)
        break
    else:
        print('Неверно. Попробуйте еще раз!')
        number = int(input('Введите число от 0 до 10: '))
else:
    print('Неверно. Попробуйте еще раз!')
    number = int(input('Введите число от 0 до 10: '))

# Задача 2

a = int(input('Введите число номер 1: '))
b = int(input('Введите число номер 2: '))


print('Число номер 1 =', (a - a) + b, 'Число номер 2 =', (b - b) + a)
