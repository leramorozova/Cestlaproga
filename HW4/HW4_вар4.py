print ('Введите число')
n=int(input())
for i in range(n):
    print('Введите слово')
    a=input()
    print ('Ваше слово:', a)
    if a=='программирование':
        break
print ('Цикл завершен')