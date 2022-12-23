# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

test_lst = [2, 1, 0, 4, 5]

def multiply_pair_numbers(list_of_nums):
    even_len = True
    if len(list_of_nums) % 2:
        a = list_of_nums.pop(len(list_of_nums) // 2)
        even_len = False
    result_lst = []
    left = 0
    right = len(list_of_nums) - 1
    for i in range(len(list_of_nums) // 2):
        result_lst.append(list_of_nums[left] * list_of_nums[right])
        left += 1
        right -= 1
    if even_len:
        print(result_lst)
    else:
        result_lst.append(a)
        print(result_lst)

print(test_lst)
multiply_pair_numbers(test_lst)
print('-' * 50)
print([2, 1, 4, 5])
multiply_pair_numbers([2, 1, 4, 5])

