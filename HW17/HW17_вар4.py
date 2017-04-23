#Программа должна обходить все дерево папок, начинающееся с той папки
#где она находится, и соообщать, на какую букву начинается название
#большинства папок (если таких много, можно печатать только одну)

import os

dirlist = [el for root, dirs, files in os.walk('.') for el in dirs]

stat = {}

letters = 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбю'

letter = [name[0].lower() for name in dirlist]

for el in letter:
    if el not in letters:
        letter.remove(el)
    if el in stat:
        stat[el] += 1
    else:
        stat[el] = 1

i = 0
res = 0
for value in stat:
    if stat[value] > i:
        i = stat[value]
        res = value

if i==0:
    print ('Названий, начинающихся с букв, похоже, тут нет :(')
else:
    print('Чаще всего названия папок начинаются с буквы:', res, '\nТакие названия встречаются', i, 'раз(a)')
