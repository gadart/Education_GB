incoming_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for names in incoming_list:
    name = names.split()[-1].title()
    print('Привет,', name)