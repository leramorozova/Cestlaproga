import random

def read_file():
    wordlist=[]
    file = open('riddles.csv', 'r', encoding='UTF-8')
    for line in file:
        linelist=line.split()
        for word in linelist:
            wordlist.append(word)
    file.close()
    return wordlist

def key_creator():
    key_list = []
    i = 0
    for word in read_file():
        if i % 2 == 0:
            key_list.append(word)
        i += 1
    return key_list

def value_creator():
    value_list=[]
    i = 0
    for word in read_file():
        if i % 2 == 1:
            value_list.append(word)
        i += 1
    return value_list

def dict_creator():
    riddles={}
    q=0
    value_list=value_creator()
    for word in key_creator():
        key=word
        value=value_list[q]
        riddles[key]=value
        q+=1
    return riddles

riddle_list=dict_creator()
dots=''
clue_list=key_creator()
clue=random.choice(clue_list)
answer=riddle_list[clue]
for letter in range (len(clue)):
    dots+='.'
print ('Угадай правильное существительное:\n', clue, dots)
user_ans=input('Введите ответ: ')
if user_ans==answer:
    print('Победа! :)')
else:
    print('Неверно! Правильный ответ -', answer+'.')
