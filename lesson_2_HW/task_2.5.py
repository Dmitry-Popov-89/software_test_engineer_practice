# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
from random import randint

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in range(len(lst)):
    lst.insert(randint(0, len(lst)-2), lst.pop(randint(0, len(lst)-1)))

print(lst)