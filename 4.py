min=int(0)
max=int(5)
import random
number = random.randint(min,max)
print(number)
def x():
    print("Введите число от",min,"до",max)
x()
guess = int(input())
if guess == number:
    print('Поздравляю, вы угадали,') # Начало нового блока
    print('(хотя и не выиграли никакого приза!)') # Конец нового блока
elif guess < number:
    print('Нет, загаданное число немного больше этого.') # Ещё один блок
# Внутри блока вы можете выполнять всё, что угодно ...
else:
    print('Нет, загаданное число немного меньше этого.')