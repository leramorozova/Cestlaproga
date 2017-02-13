import re

def read_file():
    with open ('philosophy.html', 'r', encoding='UTF-8') as file:
        text=file.read()
        file.close()
        return text

def substitution ():
    text=read_file()
    form=re.sub('философи(я|и|ю|ей|й|ями?|ях)', 'астрологи\\1', text)
    form2=re.sub('Философи(я|и|ю|ей|й|ями?|ях)', 'Астрологи\\1', form)
    form3=re.sub('Филосо́фия', 'Астрология', form2)
    form4=re.sub('ФИЛОСОФИ(И|Я)', 'АСТРОЛОГИ\\1', form3)
    return form4

def main():
    new_file=open('Астрология.html', 'w', encoding='utf-8')
    text=new_file.write(substitution())
    new_file.close()

main()
print ('А теперь попробуйте заглянуть в папку с программой и найти там файл "Астрология".')