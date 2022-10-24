# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint


user_1 = input('Ваше имя, первый игрок ?\n')
user_2 = input('Ваше имя, второй игрок ?\n')

print(f'{user_1} и {user_2} для начала игры мы\
 рандомным образом определим, кто ходит первым !')

lucky_number = randint(1,2)
if lucky_number == 1:
    player_1 = user_1
    player_2 = user_2
else: 
    player_1 = user_2
    player_2 = user_1

print(f'и первым ходит - {player_1} !')

total_sweets = 200
max_sweets = 28
index = 0

while total_sweets > 0:
    
    if index == 0:
        if total_sweets < max_sweets:
            step = int(input(f'{player_1} сколько конфет возьмешь?(не больше {total_sweets} штук): '))
            if step > total_sweets :
                step = int(input(f'{player_1} возьми меньше {total_sweets} конфет: '))
        else:
            step = int(input(f'{player_1} сколько конфет возьмешь?(не больше {max_sweets} штук): '))
            if step > max_sweets:
                step = int(input(f'{player_1} возьми меньше {max_sweets} конфет: '))
        total_sweets -= step
        if total_sweets == 0:
            print(f'Конфеты кончились !\nПобедил {player_1} ! Поздравляем !!!')
        else:
            print(f'Осталось {total_sweets} штук конфет')
            index = 1
    
    if index == 1:
        if total_sweets < max_sweets:
            step = int(input(f'{player_2} сколько конфет возьмешь?(не больше {total_sweets} штук): '))
            if step > total_sweets :
                step = int(input(f'{player_2} возьми меньше {total_sweets} конфет: '))
        else:
            step = int(input(f'{player_2} сколько конфет возьмешь?(не больше {max_sweets} штук): '))
            if step > max_sweets:
                step = int(input(f'{player_2} возьми меньше {max_sweets} конфет: '))
        total_sweets -= step
        if total_sweets == 0:
            print(f'Конфеты кончились !\nПобедил {player_2} ! Поздравляем !!!')
        else:
            print(f'Осталось {total_sweets} штук конфет')
            index = 0