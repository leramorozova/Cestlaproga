import re

def file_name():
    print ('Поместите файл в одну папку с данной программой.\nВведите имя файла, чтобы получить список словоформ:')
    name=input()
    return name

def read_file():
    wordlist=[]
    file = open(file_name(), 'r', encoding='UTF-8')
    for line in file:
        linelist=line.split()
        for word in linelist:
            word=word.lower()
            word=word.strip('.,:;"«»-?()!')
            wordlist.append(word)
    file.close()
    return wordlist

def form_finder():
    form_list=[]
    for word in read_file():
        form=re.search('(не(до)?|под)?вып[еиь]([йтлеюи]|(вш))[мшьаоиыуе]?(го|м(у|и)?[ейяюх])?(ся)?', word)
        if form!=None:
            find=form.group()
            form_list.append(word)
    return form_list

def list_without_repetitions():
    list=form_finder()
    for el in list:
        el_new=el
        for el in list:
            if el_new==el:
                list.remove(el)
    return list

for el in list_without_repetitions():
    print(el)