if __name__ == "__main__":
    pass
# Задание 12 из ЕГЭ-2025 профиль [https://math-ege.sdamgia.ru/problem?id=77429]
# Найдите наименьшее значение функции y = x^3 - 2x^2 + x + 3 на отрезке [1;4] 
import numpy as np
x_values = np.linspace(1, 4, 1000)
y_values = x_values**3 - 2*x_values**2 + x_values + 3
min_y = min(y_values)
print('Найменьшее значение:', min_y)
