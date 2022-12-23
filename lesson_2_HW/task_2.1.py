# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Без работы с методами строк.

# user_number = float(input('Введите дробное число: '))
# num_len = len(str(user_number))
# int_num = int(user_number * 10 ** (num_len - 2))
# digits_sum = 0
#
# while (int_num != 0):
#     digits_sum = digits_sum + (int_num % 10)
#     int_num //= 10
#
# print(f"Сумма цифр равна: {digits_sum}")

# -------------------------------------------------------------------------------
# Закомментированный вариант не работает с большим количеством цифр после запятой
# -------------------------------------------------------------------------------

nums_1, nums_2 = input('Введите вещественное число: ').split('.')
nums_1 = int(nums_1)
nums_2 = int(nums_2)

result_sum = 0

while (nums_1 != 0):
    result_sum = result_sum + (nums_1 % 10)
    nums_1 //= 10

while (nums_2 != 0):
    result_sum = result_sum + (nums_2 % 10)
    nums_2 //= 10

print(f"Сумма цифр равна: {result_sum}")
