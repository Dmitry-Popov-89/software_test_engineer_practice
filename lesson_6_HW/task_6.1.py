# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.

num_list = [22, 8, 13, 12, 25, 33, 19, 11, 44, 30]

def sort_numbers(some_list):
    comparing_gen = []
    for number in range(1, len(some_list)):
        comparing_gen = [some_list[idx] for idx in range(1, len(some_list)) if some_list[idx] > some_list[idx - 1]]
    return comparing_gen

sorted_list = sort_numbers(num_list)
print(sorted_list)