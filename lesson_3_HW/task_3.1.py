# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
from random import randint


def get_random_numbers_lst():
    result_lst = []
    amount = int(input('Введите желаемое количество герерируемых чисел: '))
    for i in range(amount):
        result_lst.append(randint(1, 10)) #взял диапазон 1-10 для быстрой проверки суммы
    return result_lst


def odd_positions_sum(list_of_nums):
    sum = 0
    for i in range(0, len(list_of_nums), 2):
        sum += list_of_nums[i]
    return sum


num_lst = get_random_numbers_lst()
odd_sum = odd_positions_sum(num_lst)

print(num_lst)
print(odd_sum)
