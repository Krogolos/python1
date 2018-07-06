name = input('Введите имя: ')
surname = input('Введите фамилию: ')
age = int(input('Введите возраст: '))
weight = int(input('Введите вес: '))

if age < 30:
    if weight < 50:
        print(name, surname, str(age) + 'год(а)', 'вес ' + str(weight), '- анарексия')
    elif weight > 120:
        print(name, surname, str(age) + 'год(а)', 'вес ' + str(weight), '- ожирение')
    else:
        print(name, surname, str(age) + 'год(а)', 'вес ' + str(weight), '- хорошее состояние')
elif age >= 30:
    if age >= 40:
        if weight < 50:
            print(name, surname, str(age) + 'год(а)', 'вес ' + str(weight), '- следует обратиться к врачу!')
        elif weight > 120:
            print(name, surname, str(age) + 'год(а)', 'вес ' + str(weight), '- следует обратиться к врачу!')
        else:
            print(name, surname, str(age) + 'год(а)', 'вес ' + str(weight), '- нормальное состояние')
    elif age < 40:
        if weight < 50:
            print(name, surname, str(age) + 'год(а)', 'вес ' + str(weight), '- следует заняться собой')
        elif weight > 120:
            print(name, surname, str(age) + 'год(а)', 'вес ' + str(weight), '- следует заняться собой')
        else:
            print(name, surname, str(age) + 'год(а)', 'вес ' + str(weight), '- все хорошо')
    
    
