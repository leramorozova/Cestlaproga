quan_punct=0
quan_total=0
print ('Введите путь к файлу (используйте корректные слэши и не используйте кавычкм):')
way=input()
f=open(way, 'r', encoding='utf-8')
for line in f:
    arr = line.split()
    for word in arr:
        quan_total+=1
        if word[-1]=='.' or word[-1]==',':
            continue
        else:
            quan_punct += 1
if quan_total==0:
    print ('Заданный файл пуст!')
else:
    print ('Количество слов, не оканчивающихся знаком препинания:', (quan_punct/quan_total)*100, '%')
f.close()
