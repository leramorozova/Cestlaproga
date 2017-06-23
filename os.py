import os

# Пройти по всем файлам в данной директории (и внутри всех поддтректорий)
# и распечатать названия тех файлов, в названиях которых
# а) буква А встретилась больше 3х раз:
# б) есть знаки препинания

def lists_creator():
    aaa=[]
    punct=[]
    file_list=[files for root, dirs, files in os.walk('/home/lera/Рабочий стол/Загрузки')]
    for folder in file_list:
        for file in folder:
            q_a=0
            q_punct=0
            for word in file:
                for letter in word:
                    if letter=='a' or letter =='A' or letter =='А' or letter =='а':
                        q_a+=1
                    if letter =='.' or letter ==',' or letter =='?' or letter =='!' or letter =='(' or letter == ')' or letter =='-':
                        q_punct+=1
            if q_a>3:
                aaa.append(file)
            if q_punct-1>0:
                punct.append(file)
    print ('+++++++++++++Файлы, в которых большк 3х "а":+++++++++++++')
    for el in aaa:
        print (el)
    print ('+++++++++++++Файлы со знаками препинания в названии:+++++++++++++')
    for el in punct:
        print(el)



#Написать программу, которая рисует дерево текущей папки в таком виде:
#--folder1
#   --folder4
#       file4
#       file5
#   --folder5
#--folder2
#   file2
#   file3
#--folder3

def kracuvo():
    for roots, dirs, files in os.walk('/home/lera/Рабочий стол/Загрузки'):
        for dir in dirs:
            print('--',dir)
            path='/home/lera/Рабочий стол/Загрузки'+'/'+str(dir)
            for file in os.listdir(path):
                print ('    ', file)


#def kracuvo_v2():
#    for roots, dirs, files in os.walk('/home/lera/Рабочий стол/Загрузки'):
print(os.path.join('дз ап', 'morozova3.docx'))