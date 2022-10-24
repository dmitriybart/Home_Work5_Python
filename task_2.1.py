# Игрок против "ителлекта"

from random import randint


user_1 = input('Ваше имя, первый игрок ?\n')
print('\nПротив Вас играет ИИ\n')
user_2 = "ИИ"

users = [user_1, user_2]

print(f'{user_1} и {user_2} для начала игры мы\
 рандомным образом определим, кто ходит первым !')

lucky_number = randint(0,1)

print(f'и первым ходит - {users[lucky_number]}!\n')

total_sweets = 2021
max_sweets = 28
index = 0

while total_sweets > 0:
    
    if lucky_number == 0:
        if total_sweets < max_sweets:
            step = int(input(f'{users[lucky_number]} сколько конфет возьмешь?(не больше {total_sweets} штук): '))
            if step > total_sweets :
                step = int(input(f'{users[lucky_number]} возьми меньше {total_sweets} конфет: '))
        else:
            step = int(input(f'{users[lucky_number]} сколько конфет возьмешь?(не больше {max_sweets} штук): '))
            if step > max_sweets:
                step = int(input(f'{users[lucky_number]} возьми меньше {max_sweets} конфет: '))
        total_sweets -= step
        if total_sweets == 0:
            print(f'Конфеты кончились !\nПобедил {users[lucky_number]} ! Поздравляем !!!')
        else:
            print(f'Осталось {total_sweets} штук конфет\n')
            
            lucky_number = 1
    if lucky_number == 1:
        print('Ходит ИИ ...')
        if total_sweets < 29:
                step = total_sweets
        else:
                step = total_sweets%(max_sweets+1)
                if step == -1:
                    step = max_sweets -1
                if step == 0:
                    step = max_sweets
        total_sweets -= step
        print(f'ИИ сходил на {step} конфет\n')
        if total_sweets == 0:
            print(f'Конфеты кончились !\nПобедил {users[lucky_number]} ! Поздравляем !!!')
        else:
            print(f'Осталось {total_sweets} штук конфет\n')
            lucky_number = 0