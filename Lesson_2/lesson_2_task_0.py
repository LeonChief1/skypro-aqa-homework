# Задание 0. Приведение типов

# 1. Создайте файл lesson_2_task_0.py.
# 2. Создайте переменную my_age.
# 3. Задайте значение переменной через функцию input.
# 4. Запустите скрипт и введите в консоль ваш возраст.
# 5. Выведите на экран сообщение в формате «Ваш возраст: my_age».
# 6. Сохраните в переменную my_age эту же переменную + 1.
# - Подсказка
    
#     my_age = my_age + 1
    
# 1. Выведите в консоль обновленный возраст.
# 2. Запустите скрипт и укажите ваш возраст.
# 3. Внимательно изучите текст ошибки в консоли.
# 4. Введенное значение является строкой. Необходимо преобразовать значение my_age к типу «число».

# Используйте для этого функцию int().
# Пример: my_age = int("23") #запишется число 23, а не строка “23”

# 1. Перезапустите скрипт.

my_age = input("Ваш возраст: ")

# print("Ваш возраст: " + my_age)

my_age = int(my_age) + 1

print("Ваш возраст + 1 год:", my_age)