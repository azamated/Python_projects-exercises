# -*- coding: utf-8 -*-
'''
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.

Между строками не должно быть дополнительного символа перевода строки.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import sys
file = sys.argv[1]

with open(file, 'r') as f:
    str_file = f.read().rstrip().split('\n')
    for line in str_file:
        if line.startswith('!'):
            continue
        else:
            print(line)