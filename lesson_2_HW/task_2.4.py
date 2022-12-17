# Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

test_lst = []
n = int(input('Введите N: '))


def get_user_position(test_lst, txt):
    flag = True
    position = 0
    while flag:
        position = int(input(f'Ведите {txt}: '))
        if position < 1 or position > len(test_lst):
            print(f'В списке отсутствует указанная позиция. Введите число от 1 до {len(test_lst)}')
            continue
        else:
            flag = False
    return position


for i in range(-n, n + 1):
    test_lst.append(i)

position_1 = get_user_position(test_lst, 'позицию 1')
position_2 = get_user_position(test_lst, 'позицию 2')

print(test_lst)
print(test_lst[position_1 - 1] * test_lst[position_2 - 1])
