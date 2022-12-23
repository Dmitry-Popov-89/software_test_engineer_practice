# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.


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

x_a = coordinate_input("xA")
y_a = coordinate_input("yA")
x_b = coordinate_input("xB")
y_b = coordinate_input("yB")


points_distance = (((x_a - x_b) ** 2) + ((y_a - y_b) ** 2)) ** 0.5

print(f'Расстояние между точками равно {points_distance:.3f}')