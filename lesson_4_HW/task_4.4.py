from random import randint


def create_vars(k):
    lst = []
    for i in range(k + 1):
        lst.append(randint(1, 10))
    return lst


def create_str_expr(lst):
    rev_lst = lst[::-1]
    expr = ''
    if len(rev_lst) < 1:
        expr = 'x = 0'
    else:
        for i in range(len(rev_lst)):
            if i != len(rev_lst) - 1 and rev_lst[i] != 0 and i != len(rev_lst) - 2:
                expr += f'{rev_lst[i]}x^{len(rev_lst) - i - 1}'
                if rev_lst[i + 1] != 0:
                    expr += ' + '
            elif i == len(rev_lst) - 2 and rev_lst[i] != 0:
                expr += f'{rev_lst[i]}x'
                if rev_lst[i + 1] != 0:
                    expr += ' + '
            elif i == len(rev_lst) - 1 and rev_lst[i] != 0:
                expr += f'{rev_lst[i]} = 0'
            elif i == len(rev_lst) - 1 and rev_lst[i] == 0:
                expr += ' = 0'
    return expr


def write_file_append(text):
    with open('task4.4.txt', 'a', encoding='utf-8') as f:
        f.write(text)


k = int(input("Введите натуральную степень k: "))
a = create_vars(k)
print(a)
b = create_str_expr(a)
print(b)
write_file_append(b)

