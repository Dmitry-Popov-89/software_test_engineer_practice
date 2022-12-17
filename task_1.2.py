#  Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W)

def user_input():
    values = ["W", "X", "Y", "Z"]
    result_lst = []
    for i in range(4):
        _temp = ''
        while not _temp.isdigit():
            _temp = input(f"Введите значение {values[i]}: ")
        result_lst.append(_temp)
    return result_lst


def predicate_checking(val):
    return not (val[0] and val[3]) or not val[2] or (val[1] != val[0])


statement = user_input()

if predicate_checking(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")