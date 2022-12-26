# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
from random import uniform


def real_nums_list_gen():
    flag = True
    while flag:
        try:
            lst_len = int(input('Введите количество чисел в списке: '))
            flag = False
        except(ValueError):
            print('Введите целое число!')
    result_lst = []
    for i in range(lst_len):
        result_lst.append(round(uniform(0, 100), 2))
    return result_lst


def decimal_part_max_min_difference(real_num_lst):
    dec_part_lst = []
    for i in range(len(real_num_lst)):
        dec_part_lst.append(int(str(real_num_lst[i]).split('.')[1]))
    max_dec_part = max(dec_part_lst)
    min_dec_part = min(dec_part_lst)
    print(real_num_lst)
    print(f'Min: {min_dec_part / 100}, Max: {max_dec_part / 100}. Difference: {(max_dec_part - min_dec_part) / 100}')


user_list = real_nums_list_gen()
decimal_part_max_min_difference(user_list)
