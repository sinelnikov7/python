""" number = 23
running = True
while running:
    guess = int(input('Введите целое число : '))
    if guess == number:
        print('Поздравляю, вы угадали.')
        running = False # это останавливает цикл while
    elif guess < number:
        print('Нет, загаданное число немного больше этого.')
    else:
        print('Нет, загаданное число немного меньше этого.')
else:
        print('Цикл while закончен.')
# Здесь можете выполнить всё что вам ещё нужно
print('Завершение.') """

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