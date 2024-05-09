# **Задание 3. Площадь квадрата**

# 1. Создайте файл lesson_2_task_3.py.
# 2. Напишите функцию square, принимающую 1 аргумент — сторону квадрата — и возвращающую площадь квадрата. 

# *Площадь квадрата = сторона * сторона.*

# 1. Если переданный аргумент был не целым, округлите результат вверх.

import math

kvadrat_l = [2, 2.5]

def square(kvadrat):
    area = kvadrat * kvadrat
    if not isinstance(kvadrat, int):
        area = math.ceil(area)
    return area
    
for kvadrat in kvadrat_l:
    kvadrat_area = square(kvadrat)
    print(f"Площадь квадрата со стороной {kvadrat} равна: {kvadrat_area}")