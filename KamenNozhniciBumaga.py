from random import *
 
c=0; d=0; e=0; f=0; p=0
game=True
schet=[0]
schet1=[0]

print("Добро пожаловать в игру Камень, ножницы, бумага!")
print()
ko=int(input("Выбери, до скольки очков вы будете играть: "))
print()
#Игрок выбирает 1/2/3
while game:
        a=int(input("Введи: 1 - Камень, 2 - Ножницы, 3 - Бумага "))
        print()
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
            print()
#Бот выбирает рандомный предмет
        KNB=["Камень","Ножницы","Бумага"]
        a=randint(1,3)
        if a==1:
          print("Бот выбрал: Камень")
          e=1
        if a==2:
          print("Бот выбрал: Ножницы")
          e=2
        if a==3:
          print("Бот выбрал: Бумага")
          e=3
#Находим победителя
        if f==e:
          p=0
        if f == 1 and e == 3:
          p=2
        if f == 2 and e == 1:
          p=2
        if f == 2 and e == 3:
          p=1   
        if f == 3 and e == 1:
          p=1
        if f == 3 and e == 2:
          p=2
#Выводим кто победил и выводим счёт
        if p==0:
          print("Ничья.")
          print("Твои очки:",schet)
          print("Очки бота:",schet1)
          print()
        if p==1:
          print("Вы победили!")
          schet[0]+=1
          print("Твои очки",schet)
          print("Очки бота:",schet1)
          print()
        if p==2:
          print("Победил бот.")
          schet1[0]+=1
          print("Твои очки:",schet)
          print("Очки бота:",schet1)
          print()
        if schet==[ko]:
            print("Игра закончена, Ты победил!")
            break
        if schet1==[ko]:
            print("Игра закончена, к сожалению Бот победил.")
            break




