# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

strange_nums_gen = [x for x in range(101) if x % 20 == 0 or x % 21 == 0]
print(strange_nums_gen)