import re

def reader():
    file=open('text.xml', 'r', encoding='UTF-8')
    arr=[line.strip('\n') for line in file]
    return arr

# Посчитайте среднее количество разборов (тэг ana) на слово (тэг w).

def counter_5():
    num_w=0
    num_ana=0
    for i in reader():
        form1=re.search('<w>.+</w>',i)
        form2=re.findall('ana',i)
        for el in form2:
            num_ana+=1
        if form1!=None:
            num_w+=1
    koef=num_ana/num_w
    return koef

# Составьте частотный словарь всех частей речи в тексте. Например:
# {' APRO': 5, 'S': 277, ...}. Распечайте содержимое словаря в
# отдельный файл (на каждой строке "часть речи"<табуляция>"частотность").

def freq_dict_8():
    d={}
    list=[]
    new_list=[]
    for i in reader():
        form=re.search('gr="(.+)"',i)
        if form!=None:
            list.append(form.group(1))
    for el in list:
        i = el.split(',')
        new_list.append(i)
    keys=[item[0].strip('=qwertyuiopasdfghjklzxcvbnm/<>" ') for item in new_list if item!='NUM=nom" /><ana lex="три" gr="NUM'] #тут не вышло убрать одну лишнюю фигню
    for key in keys:
        if key in d:
            d[key] += 1
        else:
            d[key] = 1
    d_file = open('d_file.txt', 'w', encoding='utf-8')
    for key in d:
        text = d_file.write(key + '\t' + str(d[key]) + ' \n')
    d_file.close()

#Найдите в тексте все существительные в творительном падеже (обратите внимание,
# что некоторые разборы омонимичные. Если хотя бы один разбор с указанием
# творительного падежа присутствует, слово берём). Запишите в отдельный файл
# найденные существительные и контекст их употребления в таком формате:
# 3 слова слева<табуляция>найденное существительное<табуляция>3 слова справа.
# За сохранение знаков препинания отдельный плюс.

def ablativus_10(): #нет табуляции и слов в некоторых строках не хватает ;(
    tripples=[]
    phrase=[]
    line_file = open('line_file.txt', 'w', encoding='utf-8')
    for idx, el in enumerate(reader()):
        if 'abl' in el:
            tripples.append(reader()[idx-3]+reader()[idx-2]+reader()[idx-1]+reader()[idx]+reader()[idx+1]+reader()[idx+2]+reader()[idx+3],)
    for el in tripples:
        word=re.findall('<w>[а-яё]+<ana',el)
        phrase.append(word)
    for i in phrase:
        line = ''
        for word in i:
            form=re.findall('[а-я]+',word)
            line+=form[0]+' '
        text = line_file.write(line + ' \n')
    line_file.close()

def main():
    print('Среднее значение тегов <ana /> на тег <w> равно:', counter_5())
    freq_dict_8()
    ablativus_10()
    print ('Загляните в папку с программой - создан новые файлы d_file.txt и line_file.txt')

main()