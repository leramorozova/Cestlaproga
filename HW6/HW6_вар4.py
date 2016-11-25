word=input('Введите слово: ')
if word:
    for i in range(len(word)):
        print (word[i:]+word[:i])
        if i>len(word)-1:
            break
else:
    print ('Нет входных данных')