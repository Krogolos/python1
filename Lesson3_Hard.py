# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

player = {'name' : input('Enter your name: '), 'health' : 100, 'damage' : 50}
enemy = {'name' : input('Enter yor name: '), 'health' : 100, 'damage' : 50}

def attacks(who_attack, who_defend):
    who_defend['health'] -= who_attack['damage']

attacks(player, enemy)
print(enemy['health'], player['health'])
 
# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.
 
# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

def generate_person_by_name(name, health = 100, damage = 50, armor = 0.7):
    return{'name': name, 'health': health, 'damage': damage, 'armor': armor}

def write_person_to_file(person):
    with open(person['name'], 'w', encoding = 'utf-8') as f:
        for key, value in person.items():
            f.write('{} {}\n'.format(key, value))

def get_person_by_filename(filename):
    person = {}
    with open(filename, encoding = 'utf-8') as f:
        for line in f:
            key, value = line.split()
            if key == 'armor':
                value = float(value)
            elif key != 'name':
                value = int(value)
            person[key] = value
    return person

def calculate_damage(damage, armor):
    return damage // armor

def attack(who_attack, who_defend):
    damage = calculate_damage(who_attack['damage'], who_defend['armor'])
    who_defend['health'] -= damage
    print('{} нанес {} урона, у {} осталось {} жизней.'.format(who_attack['name'], damage, who_defend['name'], who_defend['health']))

player_name = input('Player name: ')
enemy_name = input('Enemy name: ')

player = generate_person_by_name(player_name)
enemy = generate_person_by_name(enemy_name)

write_person_to_file(player)
write_person_to_file(enemy)

def start_game():
    player = get_person_by_filename(player_name)
    enemy = get_person_by_filename(enemy_name)
    last_attacker = enemy
    while player['health'] > 0 and enemy['health'] > 0:
        if last_attacker == player:
            attack(enemy, player)
            last_attacker = enemy
        else:
            attack(player, enemy)
            last_attacker = player
    if player['health'] > 0:
        print('Player wins')
    else:
        print('Enemy wins')
start_game()























            
