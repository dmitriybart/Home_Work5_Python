def Step_maps(step,sign):
    valid = False
    z = "XO"
    while not valid:
        if 1<=step<=9:
                if (str(place[step-1]) not in z):
                    place[place.index(step)] = sign
                    valid = True
                else:
                    print("Эта ячейка уже занята! Введите другую: ")
                    step = int(input())
                    valid = False

def Сheck_win(place):
    for i in win_comb:
        if place[i[0]] == place[i[1]] == place[i[2]]:
            return place[i[0]]
    return False

place = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win_comb = [[0,4,8], [2,4,6], [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8]]
game_over = False
userA = True
 
while game_over == False:
    print(place[0], place[1], place[2], sep = " ")
    print(place[3], place[4], place[5], sep = " ")
    print(place[6], place[7], place[8], sep = " ")
    
    if userA == True:
        sign = "X"
        step = int(input("Игрок 1, ваш ход: "))
    else:
        sign = "O"
        step = int(input("Игрок 2, ваш ход: "))
 
    Step_maps(step,sign) 
    win = Сheck_win(place)
    if win == False:
        game_over = False
    else:
        game_over = True
 
    userA = not(userA)   

if win == "X":
    win = "Игрок 1"
else:
    win = "Игрок 2"

print(place[0], place[1], place[2], sep = " ")
print(place[3], place[4], place[5], sep = " ")
print(place[6], place[7], place[8], sep = " ")

print("Победил", win) 