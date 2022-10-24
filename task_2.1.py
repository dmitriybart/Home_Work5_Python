# Игрок против "ителлекта"

from random import randint


user_1 = input('Ваше имя, первый игрок ?\n')
print('Против Вас играет ИИ')
user_2 = "ИИ"

users = [user_1, user_2]

print(f'{user_1} и {user_2} для начала игры мы\
 рандомным образом определим, кто ходит первым !')

lucky_number = randint(1,0)

print(f'и первым ходит - {users[lucky_number]} !')

total_sweets = 2021
max_sweets = 28
index = 0

