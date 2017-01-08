#Во французской поэзии допустимо чтение обычно нечитаемых гласных для соблюдения ритмики в случае необходимости
#Например, такие гласные, как 'e'
#Моя поэтическая вольность - в данных хайку все "е" на концах слов читаются и образуют слоги
#И "u" после "q"
#Извините

import random

def open_file():
    file = open('wordlist.txt', 'r', encoding='UTF-8')
    lines = file.readlines()
    file.close()
    return lines

def random_word(lines):
    ugly_word = random.choice(lines)
    word = ugly_word.strip('\n')
    return word

def syllable_counter(word):
    syl_quan=0
    for letter in word:
        if letter=='e' or letter=='y' or letter=='u' or letter=='i' or letter=='o' or letter=='a' or letter=='é' or letter=='è' or letter=='ê' or letter=='à' or letter=='â' or letter=='ù' or letter=='û' or letter=='ô' or letter=='î':
            syl_quan+=1
    return syl_quan

def line_creator(syl_number):
    syl_max = syl_number
    line = ''
    while syl_max >= 0:
        word = random_word(open_file())
        syl_quan = syllable_counter(word)
        syl_max -= syl_quan
        if syl_max > 0:
            line=line+' '+ word
            continue
        elif syl_max == 0:
            line = line + ' ' + word
            break
        elif syl_max < 0:
            line = ''
            syl_max = syl_number
            continue
    punctuation=['!','.','?']
    phrase=line[1].upper()+line[2:]+random.choice(punctuation)
    print (phrase)

def main():
        print('\nThere you can see one more perfect creation:\n')
        line_creator(5)
        line_creator(7)
        line_creator(5)

if __name__ == '__main__':
    main()