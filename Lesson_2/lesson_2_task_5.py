# **Задание 5. Месяц — сезон**

# 1. Создайте файл lesson_2_task_5.py.
# 2. Напишите функцию month_to_season(), которая принимает 1 аргумент — номер месяца — и возвращает название сезона, к которому относится этот месяц.
# Например, передаем 2, на выходе получаем «Зима».

def month_to_season(month):
    if month in (12, 1, 2):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    else:
        return "Осень"

print(month_to_season(2))  # Выведет "Зима"
print(month_to_season(4))  # Выведет "Весна"
print(month_to_season(8))  # Выведет "Лето"
print(month_to_season(11)) # Выведет "Осень"