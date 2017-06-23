import os
import re

def s_counter_5():
    s_result = open('res.txt', 'w', encoding='utf-8')
    for root, dirs, files in os.walk('news'):
        s_result = open('res.txt', 'w', encoding='utf-8')
        for file in files:
            with open(os.path.join('news',file), 'r') as f:
                file_text = f.read()
            q=0
            for line in file_text:
                if line=='.' or line=='?' or line=='!':
                    q+=1
            text=s_result.write(file +'\t'+str(q)+ '\n')
    s_result.close()
    return s_result

def table_8():
    table = open('table.csv', 'w', encoding='utf-8')
    for root, dirs, files in os.walk('news'):
        for file in files:
            with open(os.path.join('news',file), 'r') as f:
                file_text = f.read()
            info=re.findall('<title>.+</title>', file_text)
            for el in info:
                a=re.search('>([a-яА-Я]+.[a-яА-Я]+)?\.', el)
                if a!=None:
                    author=a.group(1)
                else:
                    author='no author'
                text=table.write(author+'\n')
#                t=re.search('(\..|>)[a-яА-Я\-0-9]+\.).//', el)
#                if t!=None:
#                    title=t.group()
#                print(title)
    

s_counter_5
table_8()

#<title>Андрей Бычков. Китайский лидер Цзян Цзэминь
#уходит в отставку // «ИТАР-ТАСС», 2004.09.18</title>
