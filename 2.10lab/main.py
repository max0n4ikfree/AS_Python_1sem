height = float(input("Введите рост в см: "))
if height < 0 or height > 300:
    print("Некорректный рост")
else:
    print("Рост введен корректно")

# б) Проверка веса
weight = float(input("Введите вес в кг: "))
if weight< 0 or weight > 500:
    print("Некорректный вес")
else:
    print("Вес введен корректно")

# в) Проверка температуры
temperature = float(input("Введите температуру в градусах: "))
if temperature < -273.15:
    print("Некорректная температура")
else:
    print("Температура введена корректно")
