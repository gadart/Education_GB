for i in range(100):
    i = i + 1
    if i > 4 and i < 20:
        print(i, 'процентов')
    elif i % 10 == 1:
        print(i, 'процент')
    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        print(i, 'процента')
    else:
        print(i, 'процентов')


