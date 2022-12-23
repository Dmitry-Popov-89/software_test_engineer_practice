# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

def decimal_to_bin(dec_number):
    if dec_number == 0:
        return [0]
    bin_lst = []
    while dec_number:
        bin_lst.append(dec_number % 2)
        dec_number = dec_number // 2**1
    invert_bin_lst = bin_lst[::-1]
    for i in invert_bin_lst:
        print(i, end='')

decimal_to_bin(8)
