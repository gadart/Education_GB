def number_translate(english):
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
    return numbers.get(english)


print(number_translate('five'))
print(number_translate(input('Write your number in English(0, 10): ')))
