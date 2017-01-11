def read_words():
    wordlist=[]
    file = open('austen.txt', 'r', encoding='UTF-8')
    for line in file:
        linelist=line.split()
        for word in linelist:
            wordlist.append(word)
    file.close()
    return wordlist

def counter(part):
    quan=0
    for word in read_words():
        if word[-len(part):]==part:
            quan+=1
    return quan

print ('Число форм в данном тексте, оканчивающихся на -ed: ',counter('ed'))
print ('Из них - правильные глаголы в прошедшем времени на -y:',counter('ied'))