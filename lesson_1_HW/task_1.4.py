# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quorters = {1:'x > 0, y > 0', 2:'x < 0, y > 0', 3:'x < 0, y < 0', 4:'x > 0, y < 0',}

def quorter_check():
    user_input = 0
    while user_input not in quorters.keys():
        try:
            user_input = int(input("Введите номер четверти (число от 1 до 4): "))
            print(quorters[user_input])
        except:
            print("Нет такой четверти")

quorter_check()
