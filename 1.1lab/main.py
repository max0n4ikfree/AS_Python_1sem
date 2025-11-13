import math

# Найдите длину вектора (6;8) --- https://math-ege.sdamgia.ru/problem?id=27663.
a = 6
b = 8
length = ((a**2 + b**2))
print(math.sqrt(length))

# Даны векторы a = (17;0) и b = (-1;1). Найдите длину вектора a + 12b --- https://math-ege.sdamgia.ru/problem?id=660709.
a_x = 17
a_y = 0
b_x = -1
b_y = 1
lenght_a = (a_x + 12 * (-1))
lenght_b = (a_y + 12 * 1)
answer = (lenght_a**2 + lenght_b**2)
print(math.sqrt(answer))

# Даны векторы a = (3;-2) и b = (0;1). Найдите скалярное произведение векторов a и b --- https://math-ege.sdamgia.ru/problem?id=649891.
a_x = 3
a_y = -2
b_x = 0
b_y = 1
answer = ((a_x * b_x) + (a_y * b_y))
print(answer)
