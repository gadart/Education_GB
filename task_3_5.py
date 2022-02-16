import random

NOUNS = ["автомобиль", "лес", "огонь", "город", "дом"]
ADVERBS = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, repeat=False):
    '''
    Создает случайные шутки из набора слов
    :param n: количество шуток
    :param repeat: повтор шуток
    '''
    n -= 1
    jokes = []
    if not repeat:
        nouns_copy = NOUNS.copy()
        random.shuffle(nouns_copy)
        adverbs_copy = ADVERBS.copy()
        random.shuffle(adverbs_copy)
        adjectives_copy = ADJECTIVES.copy()
        random.shuffle(adjectives_copy)
        for num, (noun, adverb, adjectiv) in enumerate(zip(nouns_copy, adverbs_copy, adjectives_copy)):
            jokes.append(f'{noun} {adjectiv} {adverb}')
            if num == n:
                break

    else:
        for _ in range(n):
            jokes.append(f'{random.choice(NOUNS)} {random.choice(ADVERBS)} {random.choice(ADJECTIVES)}')
    return jokes


print(get_jokes(int(input('Сколько шуток хотите?: '))))
