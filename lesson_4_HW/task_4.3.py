# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
from random import randint


def get_random_numbers_lst():
    result_lst = []
    amount = input('Введите желаемое количество герерируемых чисел: ')
    if not amount.isdigit() or int(amount) < 0:  # Я бы использовал try-except, но сказано было "то что умеем"(по занятиям)
        print('Некорректный ввод')
        return
    else:
        amount = int(amount)
    for i in range(amount):
        result_lst.append(randint(1, 10)) #взял диапазон 1-10 для быстрой проверки
    return result_lst


def unique_num_lst(lst):
    sorted_lst = []
    for i in range(len(lst)):
        if lst.count(lst[i]) > 1:
            continue
        else:
            sorted_lst.append(lst[i])
    return sorted_lst

list_of_nums = get_random_numbers_lst()
result_lst = unique_num_lst(list_of_nums)
print(list_of_nums)
print(result_lst)

