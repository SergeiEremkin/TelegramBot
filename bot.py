from distutils.cmd import Command
import json
from random import *
from json import *

films = []

try:
    load()
except:
    
films.append("Матрица")
films.append("Солярис")
films.append("Властелин колец")
films.append("Техасская резня бензопилой")
films.append("Санта Барбара")


def save():
    with open("films.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii=False))
        print("Наша фильмотека была успешно сохранена в файле films.json")


def load():
    global films
    with open("films.json", "r", encoding="utf-8") as fh:
        films = json.load(fh)
        print("Фильмотека была успешно загружена")


while True:
    command = input("Введите команду ")
    if command == "/start":
        print("Бот-фильмотека начал свою работу")
    elif command == "/stop":
        save()
        print("Бот остановил свою работу. Заходите еще, будем рады")
        break
    elif command == "/all":
        print("Вот текущий список фильмов")
        print(films)
    elif command == "/add":
        f = input("Введите название фильмы")
        films.append(f)
        print("Фильм был успешно добавлен в коллекцию")
    elif command == "/help":
        print("здесь какой-то мануал")
    elif command == "/delete":
        f = input("Введите название фильмы")
        try:
            films.remove(f)
            print("Фильм был удален успешно")
        except:
            print("Такого фильмы нет в фильмотеке")
    elif command == "/random":
        # rnd = randint(0, len(films)-1)
        # print("Слепой жребий показал вам -" + films[rnd])
        print("Слепой жребий показал вам -" + choice(films))
    elif command == "/save":
        save()
    elif command == "/load":
        load()
    else:
        print("Неопознанная комнада. Просьба изучить мануал /help")
