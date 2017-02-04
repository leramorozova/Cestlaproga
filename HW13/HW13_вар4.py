import re

def file_name():
    print ('Поместите файл в одну папку с данной программой.\nВведите имя файла, чтобы получить список cфер деятельности данного ученого:')
    name=input()
    return name

def reader():
    list=[]
    file = open(file_name(), 'r', encoding='UTF-8')
    for line in file:
        line=line.strip('\n')
        list.append(line)
    file.close()
    return list

def str_sphere():
    infobox=reader()
    sphere=''
    q=0
    for line in infobox:
        if 'Научная сфера:' in line:
            sphere=infobox[q+2]
            break
        else:
            q+=1
    return sphere

def main():
    form=re.findall('>[а-я -]+</a>', str_sphere())
    list=''
    for el in form:
        el=el.strip('></a')
        print (el)

main()




