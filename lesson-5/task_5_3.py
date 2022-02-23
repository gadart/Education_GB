def gen(name, klass_number):
    m = len(name) - len(klass_number)
    if m > 0:
        for t in range(m):
            klass_number.append(None)
    for tutor, klass in zip(name, klass_number):
        yield (tutor, klass)


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Олег', 'Антон', 'Артем'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

my_gen = gen(tutors, klasses)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
