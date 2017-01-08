f=open('wordlist.txt', 'r', encoding='utf-8')
for line in f:
    arr = line.split()
    for i,word in enumerate(arr):
        arr[i] = word.strip('.,?!;:-"')
    for el in arr:
        el=el.lower()
        print (el)