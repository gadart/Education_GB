list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_2 = []

for c in list_1:
    if c.isdigit():
        list_2.extend(['"', f'{int(c):02}', '"'])
    elif c.startswith('+') or c.startswith('-'):
        if c[1:].isdigit():
            list_2.extend(['"', f'{c[0]}{int(c[1]):02}', '"'])
        else:
            list_2.append(c)
    else:
        list_2.append(c)
    list_2.append(' ')

print(list_2)
list_2 = ''.join(list_2).strip()
print(list_2)