name = str(input("Как тебя ховут? "))

if name == "Вова" or  name == "Вован" :   
    print(f"Привет  {name} !")
    time=int(input("Какой сейчас час?"))
    if (time >=0 and time <=6) or (time >=22):
        print("Доброй ночи",name)
    else:
        if (time >6 and time <=11):
            print("Доброе утро",name)
        else:
            if (time >11 and time <=18):
                print("Добрый день",name)
            else:
                print("Добрый вечер",name)
else:
    print(f"Пошел на хуй {name}!")
