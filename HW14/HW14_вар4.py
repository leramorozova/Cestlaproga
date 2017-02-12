import re

def read_file():
    with open ('philosophy.html', 'r', encoding='UTF-8') as file:
        text=file.read()
        file.close()
        return text

def substitution ():
    text=read_file()
    form=re.sub('Философcк', 'Астрологическ', text)
    form2 = re.sub('философск', 'астрологическ', form)
    form3=re.sub('философ', 'астролог', form2)
    form4=re.sub('[Фф][Ии][Лл][Оо][Сс][Оо][Фф]', 'Астролог', form3)
    form5=re.sub('Филосо́фия', 'Астроло́гия', form4)
    return form5

def main():
    new_file=open('Астрология.html','w',encoding='utf-8')
    text=new_file.write(substitution())
    new_file.close()

main()
print ('А теперь попробуйте заглянуть в папку с программой и найти там файл "Астрология".')