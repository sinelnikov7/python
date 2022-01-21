""" #!/usr/bin/env python3
i = 5
print(i)
i = i + 1
print(i)
s = '''Это многострочная строка.
Это вторая её строчка.'''
print("cnhjrf",s,"wwwww")
print(4//3)
print(-4//3)
length = 5
breadth = 2
area = length * breadth
print('Площадь равна', area)
print('Периметр равен', 2 * (length + breadth))


# Перенос строки
s = 'Это строка. \
Это строка продолжается.'
print(s)

# Несколько лог строк в одной физ строке 
i = 5; print(i); """

min=0
max=5
import random
number = random.randint(0,5)
print(number)
guess = int(input('Введите целое число : от',min,"до",max))
if guess == number:
    print('Поздравляю, вы угадали,') # Начало нового блока
    print('(хотя и не выиграли никакого приза!)') # Конец нового блока
elif guess < number:
    print('Нет, загаданное число немного больше этого.') # Ещё один блок
# Внутри блока вы можете выполнять всё, что угодно ...
else:
    print('Нет, загаданное число немного меньше этого.')
# чтобы попасть сюда, guess должно быть больше, чем number