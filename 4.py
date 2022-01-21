min=int(0)
max=int(5)
import random
number = random.randint(min,max)
print(number)
def x():
    print("Введите число от",min,"до",max)
x()
guess = int(input())
while guess != number:
    if guess < number:
        print('Нет, загаданное число немного больше этого.')
        x()
        guess = int(input()) 
    else:
        print('Нет, загаданное число немного меньше этого.')
        x()
        guess = int(input())
print('Поздравляю, вы угадали,') 
print('(хотя и не выиграли никакого приза!)')