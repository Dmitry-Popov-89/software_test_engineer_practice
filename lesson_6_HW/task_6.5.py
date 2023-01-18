import random


def get_jokes(value, flag=False):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    result_list = []
    while value >= 1:
        first = random.choice(nouns)
        second = random.choice(adverbs)
        third = random.choice(adjectives)
        if flag:
            nouns.remove(first)
            adverbs.remove(second)
            adjectives.remove(third)
            result_list.append(f'{first} {second} {third}')
        else:
            result_list.append(f'{first} {second} {third}')
        value -= 1
    return print(result_list)


get_jokes(3, True)

# вариант через random.sample и zip
# def get_jokes(count, rep=None):
#     jokes = []
#     while count > 0:
#         jokes.append(list(zip(sample(nouns, k=len(nouns)), sample(adverbs, k=len(adverbs)), sample(adjectives, k=len(adjectives))))[count])
#         count -= 1
#     print(jokes)