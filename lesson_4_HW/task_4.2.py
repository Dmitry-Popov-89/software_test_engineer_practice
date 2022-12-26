# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def primfacs(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(int(i))
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(int(n))
    return primfac


print(primfacs(9990))
