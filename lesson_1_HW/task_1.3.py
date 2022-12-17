# Напишите программу, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится)

def coordinate_input(text):
    number = 0
    flag = False
    while not flag:
        number = input(f"Введите {text}: ")
        try:
            number = float(number)
            flag = True
        except Exception:
            continue
    return number


def coordinate_quorter():
    x = 0
    y = 0
    while x == 0 and y == 0:
            x = coordinate_input("X")
            y = coordinate_input("Y")
    if x > 0 and y > 0:
        print("1")
    elif x < 0 and y > 0:
        print("2")
    elif x < 0 and y < 0:
        print("3")
    elif x > 0 and y < 0:
        print("4")
    elif x == 0:
        print("Точка расположена на оси Y")
    elif y == 0:
        print("Точка расположена на оси X")


coordinate_quorter()