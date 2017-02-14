#копировать корпус в файл формата txt и поместить в одну папку с программой, назвав
#его "corp.txt"

import re

def read_file():
    with open ('corp.txt', 'r', encoding='UTF-8') as file:
        text=file.read()
        file.close()
        return text

def counter():
    file = open('corp.txt', 'r', encoding='UTF-8')
    i=1
    for line in file:
        if '</teiHeader>' not in line:
            i+=1
        else:
            break
    file.close()
    return i            

def five_points():
    new_file=open('подсчет строк.txt', 'w', encoding='utf-8')
    text=new_file.write('Число строк заголовка: ' + str(counter()))
    new_file.close()


def dictionary():
    d={}
    wordlist=[]
    lemmas=re.findall('>\w+</w>', read_file())
    for lemma in lemmas:
        lemma=lemma.strip('></w>')
        wordlist.append(lemma)
    for word in wordlist:
        if word in d:
            d[word]+=1
        else:
            d[word]=1
    return d

def eight_points():
    d=dictionary()
    dic_file=open('словарик.txt', 'w', encoding='utf-8')
    for key in d:
        text=dic_file.write(key+' - '+ str(d[key])+' \n')
    dic_file.close()

def ten_points(): #готов только массив с найденными формами
    formlist=[]
    file = open('corp.txt', 'r', encoding='UTF-8')
    for line in file:
        pronom=re.search('type="(f.h.+?)"', line)
        if pronom != None:
            find=pronom.group(1)
            formlist.append(find)
    return formlist

five_points()
eight_points()
print ('Загляните в папку с программой и попробуйте найти в ней новые txt-файл.')
print (ten_points())
