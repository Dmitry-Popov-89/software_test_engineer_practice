#  Напишите программу, удаляющую из текста все слова, содержащие "абв".
#  В тексте используется разделитель пробел.
from random import shuffle

origin_letters = ['а', 'б', 'в']
target_pattern = 'абв'

def get_text(letters_list):
    result = ''
    try:
        words_amount = int(input('Введите требуемое количество строк: '))
    except ValueError:
        print('Вводить нежно целое число! Перезапустите программу и попробуейте снова')
        raise
    for i in range(words_amount):
        shuffle(origin_letters)
        result += f'{"".join(origin_letters)} '
    return result


def delete_trget_word(my_text, terget_word):
    my_text = list(filter(lambda x: terget_word not in x, my_text.split()))
    return " ".join(my_text)

new_text = get_text(origin_letters)
print(new_text)
filtered_text = delete_trget_word(new_text, target_pattern)
print(filtered_text)
