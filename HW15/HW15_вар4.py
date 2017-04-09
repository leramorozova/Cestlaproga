import re

def file_name():
    print ('Поместите файл в одну папку с данной программой.\nВведите имя файла:')
    name=input()
    return name

def read_file():
    sent_list=[]
    file = open(file_name(), 'r', encoding='UTF-8')
    for line in file:
        linelist=line.split('.')
        for line in linelist:
            module=line.split('?')
            for sentence in module:
                sentence=sentence.split('!')
                sent_list.append(sentence)
    file.close()
    return sent_list

def cleaner():
    arr_clean=[]
    s_arr=[]
    sent_list=read_file()
    for item in sent_list:
        for sentence in item:
            s_arr.append(sentence)
    for sent in s_arr:
        sent_clean=re.sub('[\n,:—.;"”“\\«»\*\[\]]','', sent)
        if sent_clean== '' or sent_clean=='  ' or sent_clean==', ':
            continue
        else:
            arr_clean.append(sent_clean)
    return arr_clean

def main():
    sentences = cleaner()
    for sentence in sentences:
        words = sentence.split()
        dict_lower={word:len(word) for word in words}
        dict_upper={sentence:dict_lower}
        print (dict_upper)

main()
