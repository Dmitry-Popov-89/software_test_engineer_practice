# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.

user_number = int(input('Введите число: '))

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

result = factorial(user_number)

print(f'Факториалом числа {user_number} является: {result}')

# Рекурсия
# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n-1)