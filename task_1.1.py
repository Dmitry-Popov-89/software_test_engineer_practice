# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

week_days = {1:'Нет', 2:'Нет', 3:'Нет', 4:'Нет', 5:'Нет', 6:'Да', 7:'Да',}

def hollyday_check():
    user_input = 0
    while user_input not in week_days.keys():
        try:
            user_input = int(input("Введите порядковый номер дня недели (от 1 до 7): "))
            print(week_days[user_input])
        except:
            print("Нужно вводить целое число от 1 до 7")

hollyday_check()



