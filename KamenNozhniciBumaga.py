from random import *
 


#Камень - 1
#Ножницы - 2
#Бумага - 3
c=0
d=0
e=0
f=0
p=0


#Игрок выбирает 1/2/3
while True:
    while c==0:
        a=int(input("Введи: 1 - Камень, 2 - Ножницы, 3 - Бумага "))
        if a==1:
            print("Вы выбрали: Камень")
            f=1
        elif a==2:
            print("Вы выбрали: Ножницы")
            f=2
        elif a==3:
            print("Вы выбрали: Бумагу")
            f=3
        else:
            print("Ошибка, выбери число от 1 до 3!!!")

#Бот выбирает рандомный предмет
KNB=["Камень","Ножницы","Бумага"]
a=randint(1,3) 
print("Бот выбрал",KNB[a])


#Определение победителя
while True:
    if f==e:
        p=1
    if f==1 and e==2:
        p=2
    if f == 1 and e == 3:
        p=3
    if f == 2 and e == 1:
        p=3
    if f == 2 and e == 3:
        p=2   
    if f == 3 and e == 1:
        p=2
    if f == 3 and e == 2:
        p=3

    if p==1:
        print("Ничья.")
    if p==2:
        print("Ты победил!")
    if p==3:
        print("Победил бот.")






