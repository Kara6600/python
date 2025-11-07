import math

def square(side):
    # Проверяем, целое ли число
    if not isinstance(side, int):
        # Округляем вверх, если сторона не целая
        side = math.ceil(side)
    # Вычисляем площадь квадрата
    return side * side

side_input = input("Введите сторону квадрата: ")

try:
    # Преобразуем ввод в число (float, чтобы учитывать нецелые)
    side_value = float(side_input)
    area = square(side_value)
    print(f"Площадь квадрата со стороной {side_value} равна {area}")
# по приколу и на всякий случай
except ValueError:
    print("Пожалуйста, введите корректное числовое значение стороны.")