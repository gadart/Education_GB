def number_translate_adv(english):
    numbers = {'zero': 'ноль',
               'one': 'один',
               'two': 'два',
               'three': 'три',
               'four': 'четыре',
               'five': 'пять',
               'six': 'шесть',
               'seven': 'семь',
               'eigth': 'восемь',
               'nine': 'девять',
               'ten': 'десять'}
    if english.istitle() and numbers.get(english.lower()):
        return numbers.get(english.lower()).capitalize()
    else:
        return numbers.get(english)


print((number_translate_adv('Seven')))
print(number_translate_adv(input('Write your number in English(0, 10): ')))
